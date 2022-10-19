from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.       operations like CRUDing models here


class JobPost(models.Model):
    # fields
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()

# commands for migrations:
# makemigrations -> creates new migrations based on identified changes in models
# sqlmigrate -> displays the sql statement that would be triggered
# migrate -> running, applying, unapplying the migrations
# showmigrations -> lists the migrations and their statuses
