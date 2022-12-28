from django.contrib import admin
from .models import Room, Amenity

# models 파일에서 Room과 Amenity 클래스를 가져온다는 뜻


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    # 3가지 변수가 필요:
    # 1)액션을 호출하는 클래스 2)request object(액션을 호출한 유저 정보) 3)queryset(선택한 모든 객체의 리스트)
    for room in rooms:
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # admin.ModelAdmin을 상속받기 때문에, users앱의 어드민패널과는 다름. users의 어드민패널은 비밀번호를 바꿀 수 있는 form과 특별한 날짜 등, 다른 기능을 필요로 하기 때문

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        # list_display나 list_filter에 이렇게 항목을 추가하면 장고는 해당 항목을 RoomAdmin 클래스 내부에서 찾고, 없으면 Room Model에서 찾는다
        "rating",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = (
        # 기본적으로 해당 문자를 포함하는 단어를 검색하고(__contains)
        # 앞에 ^를 붙여주면 해당 문자로 시작하는 객체들을 검색(__startswith)
        # 앞에 =를 붙여주면 해당 문자와 100% 동일한 객체만을 검색(exact)
        "owner__username",  # 튜플이나 리스트 가능
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
