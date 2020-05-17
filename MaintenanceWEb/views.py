from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate

class IndexView(TemplateView):
    template_name = "index.html"


def homeView(request):
    template_name = None
    if request.user.is_authenticated():
        template_name = 'base-login.html'
    else:
        template_name = 'base.html'
    return render (request, template_name)

class JurnalView(TemplateView):
    template_name = "jurnal.html"


class CategoryView(TemplateView):
    template_name = "category.html"


class SingleView(TemplateView):
    template_name = "single.html"


class LambdaView(TemplateView):
    template_name = "cart.html"


class ProfileView(TemplateView):
    template_name = "profile.html"
