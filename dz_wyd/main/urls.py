from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user, name='add_user'),
    path('user_list/', views.user_list, name='user_list'),
]