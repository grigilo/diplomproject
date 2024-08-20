from django.contrib import admin
from ad.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
        "create_at",
    )
