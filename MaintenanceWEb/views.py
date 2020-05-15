from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class HomeView(TemplateView):
    template_name = "base.html"

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
