"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

# from .views import HomeView

urlpatterns = [
    path('', include('api.urls')),  # 새로만들어준 app의 url 기본 path설정해주기
    path('member/', include('member.urls')),
    path('admin/', admin.site.urls, name="admin"),
    path('rest-auth/', include('rest_auth.urls')),
    path('photo/', include('photo.urls')),

    # path('member/', views.index)
]
