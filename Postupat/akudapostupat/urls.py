from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('infzav/<str:university_name>/', views.infzav, name='infzav'),
    path('list/<str:category_name>/', views.list, name='list'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)