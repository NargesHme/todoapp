# Generated by Django 3.0.3 on 2021-05-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
