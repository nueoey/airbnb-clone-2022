from django.urls import path
from . import views

# 여기에 클래스를 가져오려면 뒤에 .as_view()를 붙여줘야 함
urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            },
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",  # 전체에서 한 개를 검색해서 주는 메서드
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
