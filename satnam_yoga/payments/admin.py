from django.contrib import admin
from .models import Paypal

# Register your models here.

class PaypalAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'modified')
    list_display = ('name', 'paypalPlanId')

admin.site.register(Paypal,PaypalAdmin)
