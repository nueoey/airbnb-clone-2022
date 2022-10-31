from django.db import models
from pkg_resources import cleanup_resources
from common.models import CommonModel


class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )
    # OneToOneField는 unique. 즉, ForeignKey와 달리, 이 동영상이 하나의 experience와 연결된다면 그 활동은 다른 동영상을 가질 수 없음
    def __str__(self):
        return "Video File"
