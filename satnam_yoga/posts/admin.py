from django.contrib import admin


from posts.models import Post

# Register your models here.


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    
    list_display= ('pk','user','Profile', 'title', 'photo');
    list_display_links = ('pk','user',);
    search_fields = ('user__email','user__first_name', 'user__last_name','title','user__username');
    
    
    list_filter = ('created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )
     
    fieldsets = (
    #Primer categoria
        ("Post", {
            'fields': (
            ('title','photo'),
            ),
        }
        ),

    #Segunda  categoria
    ("META-DATA",{
        'fields':(
            ('user'),
            ('created','modified'),
        ),
    }
     ),
    )
    
    readonly_fields = ('created', 'modified','user')