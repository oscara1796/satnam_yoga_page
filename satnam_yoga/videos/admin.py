from django.contrib import admin

# Register your models here.

from videos.models import Video, Category




class videoAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'image','free_seen',)
    list_display_links = ('pk','title',)
    list_editable = ( 'image',)
    search_fields = ('title','id', 'categories__name')

    list_filter = ('created',
    'modified',
    )

    readonly_fields = ('created', 'modified')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, videoAdmin)
