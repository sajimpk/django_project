from django.shortcuts import render,redirect
from contact.models import cmmt

# Create your views here.
def home(request):
   
        A = cmmt.objects.all().order_by('-id')[:10]
        return render(request,'contact/cont.html',{'tcr': A})

def ad(request):
        A = cmmt.objects.all().order_by('-id')[:10]
        if request.method == 'POST':
                name = request.POST['name']
                email = request.POST['email']
                desc = request.POST['comment']
                new_comm = cmmt(name=name,email=email,usr_inp=desc)
                new_comm.save()
        return redirect('cont')
        
        