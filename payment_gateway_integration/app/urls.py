from django.urls import path
from app import views

urlpatterns = [
    path('', views.home,name='home'), # url for payment form
	path('success/', views.success,name='success'), # url for after payment success HTML page
	path('payment/', views.payment,name='payment'), # url for razor payment gateway
    
]