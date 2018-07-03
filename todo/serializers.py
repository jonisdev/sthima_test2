from rest_framework import serializers
from .models import Task, TodoList


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        ordering = ('id',)
        fields = ('id', 'task_description', 'todo_list', 'is_done',
                  'created_at', 'due_date', 'updated_at', 'deleted_at',)
        # fields = '__all__'
        # It prevents the field to be available in method like post or put.
        read_only_fields = ('id', 'updated_at', 'deleted_at')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        ordering = ('id',)
        fields = ('id', 'list_name', 'tasks', 'created_at', 'updated_at', 'deleted_at',)
        # fields = '__all__'
        # It prevents the field to be available in method like post or put.
        read_only_fields = ('deleted_at',)
