from django.shortcuts import render, redirect
from core.models import *

# Create your views here.
def home (request):
   if request.method=="POST":
       task=request.POST.get("task") 
       data=field.objects.create(taskname=task)
       data.save()
   replace=field.objects.all()
   context={
   'replace':replace
   }
   return render(request,'todo.html',context)

def delete (request,id):
   data=field.objects.get(id=id)
   deleted= data.delete()
   if deleted:
      return redirect('home')
   return render(request,'todo.html')

def update(request,id):
   replace=field.objects.get(id=id)
   if request.method=='POST':
      update=request.POST.get("update")
      replace.taskname=update
      replace.save()
      return redirect('home')
   context={
      'replace':replace
   }
   return render(request, 'update.html',context)