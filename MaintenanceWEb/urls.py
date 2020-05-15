from django.conf.urls import url, include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from.views import IndexView,HomeView,JurnalView,CategoryView,SingleView,LambdaView,ProfileView

urlpatterns = [
    url(r'^main$', IndexView.as_view(),name='maintenance'),
    url(r'^$', HomeView.as_view(), name='Home'),
    url(r'^admin/', admin.site.urls),
    url(r'^jurnal$', JurnalView.as_view(), name='jurnal'),
    url(r'^lamda$', LambdaView.as_view(), name='lambda'),
    url(r'^myprofile$', ProfileView.as_view(), name='profile'),
    url(r'^',include('caldera.url', namespace='caldera')),
    url(r'^cart/',include('cart.url', namespace='cart')),
    url(r'^',include('user_account.url', namespace='user')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)