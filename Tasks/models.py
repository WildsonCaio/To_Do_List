from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()
    date = models.DateField()
    status = models.BooleanField()
    def __str__(self):
        return self.task
    
    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")