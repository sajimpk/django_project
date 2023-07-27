from django.contrib import admin
from about.models import Teacher
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','tid','tname','temail','tedu')

admin.site.register(Teacher,TeacherAdmin)