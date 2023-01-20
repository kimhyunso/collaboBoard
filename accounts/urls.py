from django.urls import path, include
from . import views

app_name ='accounts'

urlpatterns = [
    path('<str:ID_user>/', views.login, name='login'),
    path('create/', views.create, name='create'),
]
