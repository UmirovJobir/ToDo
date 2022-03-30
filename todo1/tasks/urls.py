from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import index, updateTask, deleteTask, login_view, logout_view, createTask

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', index, name='list'),
    path('create_task/', createTask, name='create'),
    path('update_task/<str:pk>/', updateTask, name='update_task'),
    path('delete/<str:pk>/', deleteTask, name='delete'),
]
