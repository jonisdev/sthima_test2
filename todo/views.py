# from accounts.models import User
# from accounts.serializers import UserSerializer
from datetime import datetime as dt
from django_filters import rest_framework as filters
from .models import Task, TodoList
from .serializers import TaskSerializer, TodoListSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class ListCreateTodoList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    # filter_backends = (DjangoFilterBackend,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('updated_at', 'payer_name', 'beneficiary_name',)
    # search_fields = ('updated_at', 'payer_name', 'beneficiary_name',)

    # def get_queryset(self):
    #     return TodoList.objects.filter(deleted_at=None)


class RetrieveUpdateDestroyTodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    # TODO - Implement logical exclusion
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         my_query = self.get_queryset()
    #         obj = my_query.get(pk=kwargs['pk'])
    #     except TodoList.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         if obj.deleted_at:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #         else:
    #             obj.deleted_at = dt.now()
    #             obj.save()
    #             return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # filter_backends = (DjangoFilterBackend,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('updated_at', 'payer_name', 'beneficiary_name',)
    # search_fields = ('updated_at', 'payer_name', 'beneficiary_name',)

    # def get_queryset(self):
    #     return TodoList.objects.filter(deleted_at=None)


class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # TODO - Implement logical exclusion
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         my_query = self.get_queryset()
    #         obj = my_query.get(pk=kwargs['pk'])
    #     except TodoList.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         if obj.deleted_at:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #         else:
    #             obj.deleted_at = dt.now()
    #             obj.save()
    #             return Response(status=status.HTTP_204_NO_CONTENT)

# class ListCreateUser(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     # Return empty list for get all transfers
#     # def list(self, request, *args, **kwargs):
#     #     return Response([OrderedDict()])
#
#
# class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
