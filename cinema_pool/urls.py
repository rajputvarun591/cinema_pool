from django.urls import path
from cinema_pool import views

urlpatterns = [
    path('', views.index, name='index'),
]
