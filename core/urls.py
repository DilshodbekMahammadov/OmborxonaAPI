"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sotuvchi/', SotuvchiListCreateAPIView.as_view()),
    path('sotuvchi/<int:pk>/', SotuvchiRetrieveUpdateDestroyAPIView.as_view()),
    path('mahsulot/', MahsulotListCreateAPIView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotRetrieveUpdateDestroyAPIView.as_view()),
    path('sotuv/', SotuvListCreateAPIView.as_view()),
    path('sotuv/<int:pk>/', SotuvRetrieveUpdateDestroyAPIView.as_view()),
    path('mijoz/', MijozListCreateAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozRetrieveUpdateDestroyAPIView.as_view()),
    path('bolim/', BolimListCreateAPIView.as_view()),
]
