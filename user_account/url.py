from django.conf.urls import url
from .views import loginView, logoutView, signup, profileView, editprofileView

urlpatterns = [
    url(r'^login$', loginView, name='login'),
    url(r'^logout$', logoutView, name='logout'),
    url(r'^signup$', signup, name='signup'),
    url(r'^myprofile$', profileView, name='profile'),
    url(r'^edit-profile$', editprofileView, name='edit-profile')
]
