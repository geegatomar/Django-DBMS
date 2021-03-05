from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# creating a table in the database


class Post(models.Model):
    title = models.CharField(max_length=100)
    # text field gives unlimited text space
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
