from django.conf.urls import url, include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from.views import IndexView,BaseView,LoginView,JurnalView,CategoryView,SingleView,RegisterView,LambdaView,ProfileView,mylogin

urlpatterns = [
    url(r'^main$', IndexView.as_view(),name='maintenance'),
    url(r'^base$', BaseView.as_view(), name='base'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^jurnal$', JurnalView.as_view(), name='jurnal'),
    url(r'^lamda$', LambdaView.as_view(), name='lambda'),
    url(r'^myprofile$', ProfileView.as_view(), name='profile'),
    url(r'^',include('caldera.url', namespace='caldera')),
    url(r'^cart/',include('cart.url', namespace='cart'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)