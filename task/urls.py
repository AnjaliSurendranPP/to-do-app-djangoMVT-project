from django.urls import path
from task import views

urlpatterns = [
    path('', views.get, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
]