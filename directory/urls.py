from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/models/', views.get_models, name='get_models'),
]

