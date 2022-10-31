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
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
        # 카테고리가 삭제된다고 해당 experience가 사라지는건 말이 안되므로 SET_NULL 적용, 또한 null=True, blank=True도 설정해줘야 함
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        return self.amenities.count()

    def rating(self):
        count = self.reviews.count()  # related_name을 사용하지 않았다면 review_set이라고 써야함
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in self.reviews.all().values(
                "rating"
            ):  # in 뒤는 딕셔너리(print해보면 딕셔너리임을 알 수 있음))
                # in 뒤를 self.reviews.all()로 한다면 데이터가 클 때 훨씬 더 시간이 오래 걸림
                total_rating += review["rating"]
            return round(total_rating / count, 2)


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
