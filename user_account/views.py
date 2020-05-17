from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm

# Create your views here.
def loginView(request):   
    if request.method == "POST":

        username_login = request.POST["username"]
        password_login = request.POST["password"]
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
        return redirect("Home")

    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('Home')
        else:
             return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('Home')
    else:
        form = SignUpForm()

    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('Home')
    
    return render (request, 'signup.html', {'form':form})

   
@login_required
def logoutView(request):
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect("Home")

    return render(request, "logout.html")


