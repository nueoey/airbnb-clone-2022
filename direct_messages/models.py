from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):  # 채팅방

    # rooms 폴더에도 같은 이름(Room)의 모델이 있음. 이것은 문제가 되지 않지만, 같은 이름을 가진 2개의 모델이 같은 모델(User)와 연결되어 있다는 것은 문제

    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
