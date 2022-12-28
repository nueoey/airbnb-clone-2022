from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    # "review는 1명의 user를 가진다. 그리고 1명의 user는 여러 개의 reviews를 가진다."
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        # reverse accessor는 장고에 의해 자동적으로 추가되고, related_name을 이용해 이름을 변경할 수 있음
        # 이렇게 이름을 바꿔주지 않으면 기본으로 "review_set" 이라는 이름이 적용됨
    )

    # "review는 1개의 room을 가진다. 그리고 1개의 room은 여러 개의 reviews를 가진다."
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    payload = models.TextField()  # 리뷰 내용
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} / {self.rating}⭐️"
