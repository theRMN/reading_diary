from django.contrib.auth import get_user_model
from django.db import models

from datetime import datetime


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=256)
    goal_state = models.BooleanField(default=False)


class Note(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    date = models.DateField(default=datetime.now().date())
    time = models.TimeField(default=datetime.now().time())
    text = models.TextField()
    num_pages = models.PositiveIntegerField()
