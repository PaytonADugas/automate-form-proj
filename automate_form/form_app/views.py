from django.shortcuts import render
from django.http import HttpResponse
from form_app.models import NCCS_Student, Test_model
from form_app.forms import Student_data, Test_data


def index(request):
    return render(request, 'form_app/index.html')

def form(request):
    form = Student_data()
    if request.method =='POST':
        form = Student_data(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'form_app/form.html', context={'student_form':form})

def display(request):
    student_list = NCCS_Student.objects.order_by('first_name')
    student_dict = {'students':student_list}
    return render(request, 'form_app/display.html', context=student_dict)

def student(request, slug):

    student = NCCS_Student.objects.get(first_name=slug)

    student_dict = {'student':student}
    return render(request, 'form_app/student.html', context=student_dict)
