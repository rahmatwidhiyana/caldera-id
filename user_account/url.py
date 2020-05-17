from django.conf.urls import url
from .views import loginView, logoutView, signup

urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    url(r'^login$', loginView, name='login'),
    url(r'^logout$', logoutView, name='logout'),
    url(r'^signup$', signup, name='signup')
]
