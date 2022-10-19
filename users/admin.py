from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # user 관리자패널은 다른 앱의 관리자패널과 다른 기능이 필요하므로, houses 앱 때와는 달리 UserAdmin 클래스를 상속받아야 함
    # 튜플이나 딕셔너리 등의 끝에 콤마(,)를 붙이는 목적은 vscode가 튜플과 딕셔너리를 펼쳐서 보여주게 하기 위함임
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    # 유저 리스트를 표시할 때 보이는 column을 설정하는 튜플
    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )
