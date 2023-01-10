from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


# ModelSerializer를 사용하기 때문에, id, created_at, updated_at은 이미 read-only인 property로 설정되어 있음


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )
        # depth = 1  장고와 DRF가 "owner"의 ID를 보고 이 object를 serialize한 후, 그 데이터를 ID 대신에 넣어줄 것
        # depth = 1의 단점은 커스터마이즈 할 수 없다는 것. 따라서, 모든 항목들이 다 나옴

        # serializer를 확장하고 싶지만 모든 것을 다 보여주고 싶지는 않을 때는 serializer를 커스터마이징해야 함
        # 예를 들어, 유저 정보를 모두 보여주고 싶지 않으므로, users폴더 내에 커스텀 serializer를 만든다.
        # 그 후, 만든 TinyUserSerializer를 불러오고,


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(
        read_only=True  # 이렇게 하면 방을 생성할 때 serializer가 owner에 대한 정보를 요구하지 않음
    )
    # owner필드를 serialize할 때는 TinyUserSerializer 사용하라는 뜻. 아래의 amenities와 category 필드도 마찬가지

    # 방을 생성할 때 amenities와 category는 nested field 형태로 입력해야 하는데, serializer는 그런 기능이 없기 때문에 오류 발생
    # 따라서, 1)serializer를 위해 정확한 create 메서드를 직접 작성하거나, 2)필드를 read_only로 설정해줘야 함
    # read_only일 경우, serializer가 해당 필드를 validation해줄 수 없기 때문에, 직접 validation 과정을 만들어줘야 함
    amenities = AmenitySerializer(read_only=True, many=True)  #
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    # SerializerMethodField는 rating의 값을 계산할 메서드를 만들 거라는 뜻
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

    # 메서드의 이름은 반드시 속성의 이름 앞에 get_을 붙인 것이어야 함
    # 두번째 argument는 현재 serializing하고 있는 오브젝트
    def get_rating(self, room):
        print(self.context)
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_is_liked(self, room):
        request = self.context["request"]
        # request를 받아오는 이유는, 어떤 user가 이 방을 보고있는지 확인하기 위해서임
        return Wishlist.objects.filter(
            user=request.user,
            rooms__id=room.pk,
        ).exists()
        # .get()을 쓰지 않은 이유는 한 유저가 여러 개의 wishlist를 가지고 있을 수 있기 때문
