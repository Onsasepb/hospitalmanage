
from django.contrib import admin
from django.urls import path
from yummyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.index, name='homepage'),
    path('innerpage/', views.innerpage, name='innerpage'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]
