from django.contrib import admin
from .models import Experience, Perk


@admin.register(Experience)  # Experience 클래스가 아래의 어드민패널을 컨트롤한다는 뜻
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
    )
