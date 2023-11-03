from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    # id
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    favourite_by = models.ManyToManyField(User, related_name='favourite_notes', blank=True)
