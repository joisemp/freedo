from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
from django.utils.text import slugify
from config.utils import generate_unique_slug


User = get_user_model()


class Project(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = generate_unique_slug(self, base_slug)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

