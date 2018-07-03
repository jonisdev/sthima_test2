from django.db import models
from model_utils import Choices
from datetime import datetime as dt
from django.conf import settings


class TodoList(models.Model):

    # user_id = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     verbose_name='User',
    #     related_name='transfers',
    #     on_delete=models.CASCADE
    # )

    list_name = models.CharField(
        verbose_name='List Name',
        max_length=200,
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True
    )

    deleted_at = models.DateTimeField(
        verbose_name='Deleted at',
        null=True,
        blank=True,
    )

    def __repr__(self):
        return self.list_name

    def __str__(self):
        return self.list_name


class Task(models.Model):
    task_description = models.CharField(
        verbose_name="Task Description",
        max_length=128
    )

    todo_list = models.ForeignKey(
        TodoList,
        verbose_name='Todo List',
        related_name='tasks',
        on_delete=models.CASCADE
    )

    is_done = models.BooleanField(
        verbose_name='Is Done',
        default=False
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True
    )

    due_date = models.DateTimeField(
        verbose_name='Due Date',
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True
    )

    deleted_at = models.DateTimeField(
        verbose_name='Deleted at',
        null=True,
        blank=True,
    )

    def set_task_done_status(self):
        self.is_done = True

    def __repr__(self): 
        return self.task_description

    def __str__(self):
        return self.task_description

    # def __repr__(self):
    #     return self.payer_name

    # def save(self, *args, **kwargs):
    #     self.set_transfer_type()
    #     self.set_transfer_status()
    #     super(Todo, self).save(*args, **kwargs)
