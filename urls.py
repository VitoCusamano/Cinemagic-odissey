# django_blog/urls.py

from django.contrib import admin
from django.urls import path,include
from .views import about
from .views import home_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .views import criterias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),  
    path('article',include('article.url')),
    path('',home_page , name='home_page'),  
    path("criteria/",criterias,name='criterias')
   
    
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


