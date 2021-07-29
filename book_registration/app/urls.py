from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register,name='register'),
    path('', views.show,name='home'),
    path('search/', views.search,name='search'),
    path('search1/', views.search,name='search1'),
    ]