from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    verbose_name = "Direct Messages"  # 제목에 Direct_Messages로 표시되는 것을 수정
