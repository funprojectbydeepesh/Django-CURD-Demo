from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



# Student database model to store the date 

class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Full Name'))
    student_code = models.CharField(max_length=100, verbose_name=_('Student Code'))
    course = models.CharField(max_length=100, verbose_name=_('Chosen Course'))
    course_code = models.CharField(max_length=100, verbose_name=_('Course Code'))
    major_subject = models.CharField(max_length=100, verbose_name=_('Major Subject'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'))


    def __str__(self):
        return f'{self.name}'

    
