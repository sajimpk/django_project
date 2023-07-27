
from django.shortcuts import render , redirect
# Create your views here.
def login(request):
        return render(request,'login/index.html')

def reg(request):
        return render(request,'regform/index.html')



# if request.method == 'POST':
#                 name = request.POST['name']
#                 email = request.POST['email']
#                 desc = request.POST['comment']
#                 new_comm = cmmt(name=name,email=email,usr_inp=desc)
#                 new_comm.save()