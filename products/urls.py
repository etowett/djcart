from django.urls import path

from django.urls import re_path as url
from . import views

app_name = 'products'


urlpatterns = [
    url(r'^$', views.product_list, name='list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='details'),
]
