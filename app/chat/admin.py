from django.contrib import admin
from .models import ChatRoom


@admin.register(ChatRoom)
class CommentAdmin(admin.ModelAdmin):
    pass