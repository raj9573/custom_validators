from django.shortcuts import render

# Create your views here.

from app.forms import userform

from django.http import HttpResponse

def User_Form(request):

    uf  = userform()

    if request.method == 'POST':

        ufd = userform(request.POST)

        
        if ufd.is_valid():
            return HttpResponse("data validated")

        else:
            return HttpResponse("data is not validated")


        # return HttpResponse("ppost method called")



    return render(request,'form.html',{'uf':uf})
