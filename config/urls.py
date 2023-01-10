"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 유저가 해당 url로 접근했을 때 장고가 실행하는 함수들이 적혀있음

from django.contrib import admin
from django.urls import path, include
from rooms import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path함수의 첫번째 argument는 주소, 두번째 argument는 그때 실행될 함수
    # 주소 뒤에는 반드시 /가 붙어야 함. 빼먹으면 오류 발생!
    path("admin/", admin.site.urls),
    path(
        "api/v1/rooms/", include("rooms.urls")
    ),  # /rooms/ (뒤에 뭐가 붙든 모두)에 접근한다면 rooms앱의 urls.py를 찾아보라는 뜻
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists/", include("wishlists.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 이렇게 api/버전/앱이름 형식으로 주소를 만들어주는 것이 좋음
