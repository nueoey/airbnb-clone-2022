from django.urls import path
from . import views


urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
    path("amenities/", views.Amenities.as_view()),
    # 이 url은 이미 rooms/로 들어온 url이기 때문에, 그냥 ""만 적어주는 것은 "rooms/"와 같음
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),  # <변수의 type:변수의 이름>
]
