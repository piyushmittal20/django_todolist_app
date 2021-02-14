from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=1000)
    is_urgent = models.BooleanField(blank=True)
    
    def __str__(self):
        return self.task_name
