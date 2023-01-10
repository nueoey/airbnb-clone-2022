from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlist


class WishlistSerializer(ModelSerializer):

    # WishlistSerializer는 RoomListSerializer를 사용하는데, RoomListSerializer는 get_is_owner 메서드에서 context에 있는 request 객체를 필요로 함
    # 그런데 WishlistSerializer에는 context 객체가 없기 때문에, Wishlists 클래스의 get 메서드에 context를 보내줘야 함
    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "rooms",
        )
