from django.urls import path
from .views import api_home, get_tasks, create_task, get_date
from . import views

urlpatterns = [
    path('', api_home, name='api_home'),  # Default endpoint for /api/
    path('date/', get_date, name= 'get_date'),
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/create/', create_task, name='create_task'),
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
]