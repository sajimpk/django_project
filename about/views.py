from django.shortcuts import render
from about.models import Teacher
# Create your views here.
def home(request):
   
    A = Teacher.objects.all()
    return render(request,'about/about.html',{'tcr': A})