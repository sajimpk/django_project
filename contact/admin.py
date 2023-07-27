from django.contrib import admin
from contact.models import cmmt
# Register your models here.
class showAdmin(admin.ModelAdmin):
    list_display=('id','name','email','usr_inp','time')
admin.site.register(cmmt,showAdmin)