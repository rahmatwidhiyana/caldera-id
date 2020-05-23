from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profileView(request):
    return render(request, "profile.html")

@login_required
def editprofileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            # return redirect()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'edit_profile.html', context)