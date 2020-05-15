from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginView(request):
    if request.method == "POST":

        username_login = request.POST["username"]
        password_login = request.POST["password"]
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
        return redirect("Home")

    return render(request, "login.html")


def logoutView(request):
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect("Home")

    return render(request, "logout.html")

