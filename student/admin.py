from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','student_code','course','course_code','major_subject')
    list_display_links =  ('name',)
    search_fields = ('name','student_code','course_code')


admin.site.register(Student,StudentAdmin)
