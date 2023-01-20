from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jugi/', include('board.urls')),
    path('accounts/', include('accounts.urls')),
]
