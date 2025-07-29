from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('studentdetail /<int:pk>',views.student_detail, name='student_detail'),
    path('studentdelete /<int:pk>',views.student_delete, name='student_delete'),
    path('add_student',views.add_student, name='add_student'),
    path('update/<int:pk>',views.update_student, name='update_student'),
]