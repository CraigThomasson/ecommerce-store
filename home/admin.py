from django.contrib import admin
from .models import News_letter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
    )


admin.site.register(News_letter, NewsLetterAdmin)
