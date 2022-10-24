from django.db import models
from common.models import CommonModel

# common 앱의 models.py에서 CommonModel 클래스를 import


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self):
        return f"{self.kind.title()}: {self.name}"
        # title은 문자열의 메서드로, 첫글자를 대문자로 바꿔줌

    class Meta:
        verbose_name_plural = "Categories"
