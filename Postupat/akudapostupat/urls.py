from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('infzav/<str:university_name>/', views.infzav, name='infzav'),
    path('list/<str:category_name>/', views.list, name='list'),
]