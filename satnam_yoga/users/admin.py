
#Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#My imports
from users.models import Profile

# Register your models here.

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display= ('pk','user', 'phone_number', 'image');
    list_display_links = ('pk','user',)
    list_editable = ('phone_number', 'image')
    search_fields = ('user__email','user__first_name', 'user__last_name','phone_number','user__username')

    list_filter = ('created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )


    readonly_fields = ('created', 'modified')


    fieldsets = (
    #primer categoria

    ("Profile",
    {
    'fields':(
    ('user','image'),
    ),
    }
    ),
    #Segunda categoria
    ("Extra info",{
    'fields':(
        ('phone_number'),
    ),
    }),

    #Tercera categoria
    ("META_DATA",{
        "fields":(
            ('created', 'modified'),
        ),
    })
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete= False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    inlines =(ProfileInline),
    list_display = (
    'username',
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
