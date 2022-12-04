from rest_framework.serializers import ModelSerializer
from .models import User


# model의 관계를 확장하고 싶지만, 유저 정보를 모두 다 보여주고 싶지 않을 때 serializer를 커스터마이징 하기
# 보여주고 싶은 필드만 보이도록 설정


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )
