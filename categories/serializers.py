from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    # Category의 필드 중 어느 것을 보여줄지 명시해야 함

    # 이렇게 쓰는것만으로도 serializer는 Category 모델을 위한 serializer를 만들고, create, update 메서드를 만들어줌
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )

    # 어떤 필드를 보이게 할 지 정해주지 않으면 오류 발생
    # 따라서, fields = ("", "", ...) 나 exclude = ("", "", ...) 로 보이게 할 필드를 지정해줘야 함
    # 모든 필드를 보이게 하고 싶으면 fields = "__all__"
