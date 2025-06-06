"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from home.views import *
from recipie.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from report_card.views import *
from django.shortcuts import redirect

urlpatterns = [
    #path ('', home, name = "home"),
    #path('success-url/', success, name= "success_page"),
    #path('render/', render_req, name = "render"),
    #path('about/', about, name="about"),
    #path('help/', help, name="help"),
    #path('another/', another, name='another_res'),
    path('', lambda request: redirect('login/')),
    path('recipie/', recipies, name='recipies'),
    path('delete/<id>/', delete, name= 'delete_recipie'),
    path('update/<id>/', update, name="updation"),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    #path('report/', report, name='report'),
    #path('result/<roll_number>', see_marks, name='result'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
