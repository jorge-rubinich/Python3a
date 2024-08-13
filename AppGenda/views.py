from django.shortcuts import render
from django.http import HttpResponse
from AppGenda.models import ToDo

# Create your views here.
def inicio(request):
    return render(request,'index.html')
    
           
def todo(request):
    tasks= ToDo.objects.all()

    return render(request, 'todo.html', {'tasks': tasks})

def duedates(request):
    return render(request, 'duedates.html')

def ToDoForm(request):
    if request.method== 'POST':
        # is a POST
        a=False
    else:
        # is a get.
        a=True
