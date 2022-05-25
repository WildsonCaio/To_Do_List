from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('finish_task/<int:id>', views.finish_task, name='finish_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
]