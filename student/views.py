from django.shortcuts import render , redirect
from .models import Student
from django.contrib import messages
from .forms import StudentForm


def home(request):
    students = Student.objects.all()
    return render(request,'home.html', {'students':students})


def student_detail(request,pk):
    student = Student.objects.get(id=pk)
    return render(request, 'studentdetail.html', {'student':student})

def student_delete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    messages.warning(request,'Record has been deleted')
    return redirect('home')

def add_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Data is store in database.')
            return redirect('home')

    return render(request, 'add_student.html', {'form':form})

def update_student(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Data is updated')
            return redirect('home')
    return render(request,'update_student.html',{'form':form})