from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = (
            "entire_place",
            "Entire Place",
        )
        PRIVATE_ROOM = (
            "private_room",
            "Private Room",
        )
        SHARED_ROOM = (
            "shared_room",
            "Shared Room",
        )

    name = models.CharField(
        max_length=180,
        default="",
    )  # 이미 추가해둔 방이 있기 때문에 default="" 넣어줌
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    def __str__(self):
        return self.name


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        default="",  # null=True 써도 관계없음: DB에서 null일 수 있다는 의미
        blank=True,  # 장고 form에서 공백을 의미
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
