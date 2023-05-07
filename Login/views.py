from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import Register

# Create your views here.

def loginpage(request):
    if (request.method == "POST"):
       form = LoginForm(request.POST)

       if form.is_valid():
        user = Register.objects.filter(Username = form.cleaned_data['Username'],
                                    Password =form.cleaned_data["Password"]).exists()
        if user:
         return HttpResponseRedirect("/tododetails")
        else:
           return HttpResponse("Username or Password is incorrect")
    else:  
     form = LoginForm()
    return render(request, 'LoginForm.html',{
        "loginDetails": form
    })

def signup(request):
    if (request.method == "POST"):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save();
            return HttpResponse("Submitted Successfully");
    else:
     form = RegisterForm()
    return render(request, 'Register.html', {
        "RegisterDetails": form
    })

def logout(request):
   return HttpResponseRedirect("/Login")