from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
   class Meta():
      model = Student
      fields = '__all__'

    

   def __init__(self,*args, **kwargs):
      super(StudentForm, self).__init__(*args, **kwargs)

      for field in self.fields:
         self.fields[field].widget.attrs['class'] = 'form-control'
         