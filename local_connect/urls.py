
from django.urls import path
from local_connect import views

urlpatterns = [
    path('', views.login, name='login'),
]
