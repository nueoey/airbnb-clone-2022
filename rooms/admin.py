from django.contrib import admin
from .models import Room, Amenity

# models 파일에서 Room과 Amenity 클래스를 가져온다는 뜻


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # admin.ModelAdmin을 상속받기 때문에, users앱의 어드민패널과는 다름. users의 어드민패널은 비밀번호를 바꿀 수 있는 form과 특별한 날짜 등, 다른 기능을 필요로 하기 때문
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
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
