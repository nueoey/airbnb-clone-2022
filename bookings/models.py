from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,  # Experience 예약일 경우에는 room은 빈칸이어야 하므로
        blank=True,
        on_delete=models.SET_NULL,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    check_in = models.DateField(
        null=True,  # Experience 예약일 경우에는 room은 빈칸이어야 하므로
        blank=True,
    )
    check_out = models.DateField(
        null=True,  # Experience 예약일 경우에는 room은 빈칸이어야 하므로
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,  # Room 예약일 경우에는 room은 빈칸이어야 하므로
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"
