from django.conf import settings
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='threads')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    created = models.DateField(auto_now_add=True)
