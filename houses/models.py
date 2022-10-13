from django.db import models

# Create your models here.
class House(models.Model):
    # models 모듈에서 Model 클래스를 상속

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    # 길이가 약간 짧거나 어느정도 제한 있는 텍스트
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only"
    )
    description = models.TextField()
    # 길이가 긴 텍스트
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house allow pets?"
    )

    def __str__(self):
        return self.name
