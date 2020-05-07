from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login

class IndexView(TemplateView):
    template_name='index.html'

class BaseView(TemplateView):
    template_name='base.html'  

class LoginView(TemplateView):
    template_name='login.html'

class RegisterView(TemplateView):
    template_name='register.html'

def mylogin(request):
    if request.method == "POST":
        print(request.POST)

    return render(request,'base.html')

class JurnalView(TemplateView):
    template_name='jurnal.html'

class CategoryView(TemplateView):
    template_name='category.html'
 
class SingleView(TemplateView):
    template_name='single.html'

class LambdaView(TemplateView):
    template_name='cart.html'
    
class ProfileView(TemplateView):
    template_name='profile.html'
