# Generated by Django 2.0.6 on 2018-06-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_title',
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.CharField(max_length=128, verbose_name='Task Description'),
        ),
    ]
