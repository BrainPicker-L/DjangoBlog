"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mysite import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

urlpatterns = [
    path('666admin666/', admin.site.urls),
    path('',views.blog_list,name="blog_list"),
    path('blog/<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('like_change', views.like_change,name="like_change"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)