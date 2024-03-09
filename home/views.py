from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Dates
from django.http import JsonResponse

def app(request):
    return render(request,'index.html')

def register_form_submission(request):
    if request.method=='POST':
        var1=Dates(studentName=request.POST.get('studentName'),
                   studentID=request.POST.get('studentID'),
                   email=request.POST.get('email'),
                   contact=request.POST.get('contact'))
        var1.save()
        return render(request,'index.html')
