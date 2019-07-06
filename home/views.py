from django.shortcuts import render,redirect
from home.forms import StudentSearchForm,StudentEditModelForm,StudentCreateForm
from home.models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    del request.session['id']
    if request.session == 1:
        if request.method=='POST':
            search=StudentSearchForm(request.POST)
            if search.is_valid():
                value=search.cleaned_data.get('q')
                result=Student.objects.filter(student_name=value)
                return render(request,'home.html',{'result':result,'form':StudentSearchForm()})
        else:
            form=StudentSearchForm()
            results=Student.objects.all()
            return render(request,'home.html',{'form':form,'results':results})

def deletestudent(request,id):
    result= Student.objects.get(id= id)
    result.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('/')

def editstudent(request,id):
    student = Student.objects.get(id=id)
    if request.method =='POST':
        modelform=StudentEditModelForm(request.POST, instance=student)
        if modelform.is_valid():
            modelform.save()
            return redirect('/')
    else:
        modelform= StudentEditModelForm(instance=student)
        return render(request,'edit.html',{'form':modelform})

def createstudent(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            student = Student.objects.create(student_name = form.cleaned_data.get('student_name'),
            department = form.cleaned_data.get('department'))
            student.save()
            messages.success(request,'Created Successfully!')
            return redirect('/')
    else:
        form = StudentCreateForm()
        return render(request,'create.html',{'form':form},)



    