from django.conf.urls import url
from .views import loginView, logoutView

urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    url(r'^login$', loginView, name='login'),
    url(r'^logout$', logoutView, name='logout')
]
