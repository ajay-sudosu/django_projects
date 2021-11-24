from django.urls import path
import app.views as app_views

urlpatterns = [
    path('',app_views.home,name='home'),
]
