from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
    
