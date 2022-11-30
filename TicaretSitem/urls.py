"""TicaretSitem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp.views import *
from account.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', alibaba, name='Alibaba'),
    path('kategori/<str:kategoriId>', kategori , name='kategori'),
    path('login/' , login_request , name='login' ),
    path('register/' , register_request , name='register' ),
    path('logout/' , logout_request , name='logout' ),
    path('search/' , search , name='search'),
    path('marka/<str:markaId>' , marka , name='marka'),
    path('urundetay/<str:urunId>', urunDetay , name='urundetay') ,
    path('create/' , create , name='create'),
    path('sepet/' , sepet , name='sepet'),
    path('delete<int:id>/' , deleteUrun , name='delete'),
    path('favori/' , favori , name='favori'),
    path('deletefav<int:id>/' , deletefav , name='deletefav')
    
   
    
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
