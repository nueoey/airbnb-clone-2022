from django.utils import timezone
from rest_framework import serializers
from .models import Booking

# 아래의 PublicBookingSerializer를 사용하면 사실상 유저가 guest만 입력해도 새로운 booking이 post가 됨(pk는 read only, 나머지 필드는 모두 필수가 아니므로)
# 이를 막기 위해, post할 때 사용할 용도로 CreateRoomBookingSerializer를 따로 만드는 것
class CreateRoomBookingSerializer(serializers.ModelSerializer):

    # 이렇게 함으로써 디폴트로 아래 두 필드의 값은 required(필수)가 됨
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    # 특정 필드에 원하는 검증과정을 만들고 싶으면, validate_필드명 적어주면 됨
    # 이 메서드는 자동적으로 불러져서, 검증하고 싶은 것의 value를 줌
    def validate_check_in(self, value):  # value는 validate하고 싶은 부분의 value
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value  # 이 메서드가 value를 반환하면 검증과정이 성공했다는 뜻

    def validate_check_out(self, value):  # value는 validate하고 싶은 부분의 value
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking

        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
