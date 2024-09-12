from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


# ...и регистрируем её в админке:
admin.site.register(Tag, TagAdmin)
