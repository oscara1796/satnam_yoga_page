from django.contrib import admin

# Register your models here.

from videos.models import Video


@admin.register(Video)

class videoAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'image', 'upload')
    list_display_links = ('pk','title',)
    list_editable = ( 'image', 'upload')
    search_fields = ('title',)

    list_filter = ('created',
    'modified',
    )

    readonly_fields = ('created', 'modified')
