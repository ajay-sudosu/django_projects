from django.urls import path

from . import views


urlpatterns = [
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
