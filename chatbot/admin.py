from django.contrib import admin
from .models import Chat


# Customizing the Admin Site :
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "message",
        "response",
        "created_at",
    ]

    list_filter = [
        "message",
        "response",
    ]

    search_fields = [
        "message",
        "response",
    ]

    date_hierarchy = "created_at"


admin.site.site_header = "Chatbot Admin"
admin.site.site_title = "OpenAI Chatbot Clone"
admin.site.index_title = "Welcome to Django Chat"
