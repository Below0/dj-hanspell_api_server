import base64

from django.conf import settings
from django.db import models
from django.utils import timezone


class Text(models.Model):
    original = models.TextField()
    checked = models.TextField()
    errors = models.IntegerField(default=0)

    def __str__(self):
        return self.original


class Word(models.Model):
    word_id = models.CharField(max_length=60)
    correct = models.CharField(max_length=60)
    count = models.IntegerField(default=1)

    def __str__(self):
        return base64.b85decode(self.word_id).decode()
