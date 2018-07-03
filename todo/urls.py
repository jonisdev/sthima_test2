from django.urls import path
from .views import (RetrieveUpdateDestroyTodoList, ListCreateTodoList,
                    RetrieveUpdateDestroyTask, ListCreateTask)
from django.views.generic.base import TemplateView


app_name = 'todo'

urlpatterns = [
    path('api/v1/todolists/', ListCreateTodoList.as_view(),
         name='get_post_todolists'),

    path('api/v1/todolists/<int:pk>',
         RetrieveUpdateDestroyTodoList.as_view(),
         name='get_put_delete_todolists'),

    path('api/v1/tasks/', ListCreateTask.as_view(),
         name='get_post_tasks'),

    path('api/v1/tasks/<int:pk>',
         RetrieveUpdateDestroyTask.as_view(),
         name='get_put_delete_tasks'),

    path('home/', TemplateView.as_view(template_name='index.html'), name='home')
]
