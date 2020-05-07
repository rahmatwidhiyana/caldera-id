from django.conf.urls import url
# from django.core.urlresolvers import reverse 
from.import views

app_name = 'shop'

urlpatterns = [
    url(r'kaos$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+/$)', views.product_list_by_category, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
] 
