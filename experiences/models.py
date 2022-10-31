from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experiences Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    # DateField는 일,월,연도 / TimeField는 일,월,연도,시간,분,초
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
        # 카테고리가 삭제된다고 해당 experience가 사라지는건 말이 안되므로 SET_NULL 적용, 또한 null=True, blank=True도 설정해줘야 함
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        null=True,  # default=""도 무방함
    )
    explanation = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
