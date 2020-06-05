from django.conf.urls import url
from .views import product_list, product_list_by_category, product_detail

app_name = 'shop'

urlpatterns = [
    url(r'kaos$',product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',product_list_by_category, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',product_detail, name='product_detail')
] 
