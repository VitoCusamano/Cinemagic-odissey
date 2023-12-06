from django.urls import path
from .views import article_list
from .views import article_detail
from django.urls import re_path



#from .views import about

app_name='articles'

urlpatterns = [ 
    path('',article_list , name='list'), 
    re_path(r'^(?P<slug>[\w-]+)/?$', article_detail, name='detail'),
    ]   