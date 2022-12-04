# 유저가 특정 url에 접근했을 때 작동하는 함수
# urls.py로 import해서 사용할 것이기 때문에, 이 파일의 이름이 꼭 views여야 할 필요는 없음


from rest_framework.views import APIView
from django.db import transaction
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Room, Amenity
from categories.models import Category
from .serializers import RoomListSerializer, RoomDetailSerializer, AmenitySerializer

# 모든 view function은 request를 받음


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )  # partial update하는 법!
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:  # 유저가 보낸 데이터에 "category" 항목이 없으면 에러 발생시킴
                    raise ParseError("Category is required.")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        # category kind가 EXPERIENCES일 경우 에러 발생시킴
                        raise ParseError("The category kind should be 'rooms'.")
                except Category.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("Category not found")
                try:
                    with transaction.atomic():  # 코드 중 하나라도 실패한다면 그 시점에 DB에서 변경된 사항들이 모두 되돌려지게 할 수 있음
                        room = serializer.save(
                            owner=request.user,  # owner는 이 url을 호출한 유저라는 뜻
                            category=category,
                        )
                        # 유저 데이터로만 serializer를 생성해서 save 메서드를 호출하면, 자동으로 serializer의 create 메서드 호출됨
                        # .save() 괄호 안에 추가하는 무엇이든 create 메서드의 validated_data에 추가됨
                        # 즉, request.data에 괄호 안의 데이터를 포함한 모든 validated_data를 가지고 방을 생성해 줌

                        # owner와 category는 Foreign Key임에 반해, amenities는 ManyToMany 필드임에 유의
                        # 따라서, 방이 생성된 다음 room.amenities.add()를 사용하여 amenity를 추가해줘야 함
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:  # amenities는 리스트이기 때문에 가능
                            amenity = Amenity.objects.get(
                                pk=amenity_pk
                            )  # object가 아님에 주의!
                            room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():

            if "amenities" in request.data:
                amenities = request.data.get("amenities")
                try:
                    room.amenities.clear()
                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenities.add(amenity)
                except Exception:
                    raise ParseError("Amenity not found")

            if "category" in request.data:
                category_pk = request.data.get("category")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        # category kind가 EXPERIENCES일 경우 에러 발생시킴
                        raise ParseError("The category kind should be 'rooms'.")
                    room.category = category

                except Category.DoesNotExist:  # 존재하지 않는 category id를 입력하면 에러 발생시킴
                    raise ParseError("Category not found")

            updated_room = serializer.save()

            return Response(RoomDetailSerializer(updated_room).data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        # request에는 자동으로 request.user가 포함되어 있음. 만약 유저가 로그인되었다면, 장고는 거기에 현재 로그인중인 유저를 넣어줄 것임
        if not request.user.is_authenticated:  # 로그인 x 상태일 때
            raise NotAuthenticated
        # 아래에 elif를 사용하지 않는 이유는, elif를 사용할 경우 위의 if절이 해당되면 elif절은 작동하지 않을 것이기 때문. 위 아래 모두 작동하기 원하기 때문에 if를 사용
        if room.owner != request.user:  # 로그인중인 유저가 방의 owner가 아닐 때
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)
