from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    USER = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title