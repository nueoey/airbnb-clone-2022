from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)  # 뒤에 괄호를 빼먹으면 작동하지 않음 주의!

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )
