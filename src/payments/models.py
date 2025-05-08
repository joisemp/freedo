from django.db import models
from projects.models import Project
from django.utils.text import slugify
from config.utils import generate_unique_slug


class Payment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('upi', 'UPI'),
    ]
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = f"{slugify(self.project.title)}-{self.date}"
            self.slug = generate_unique_slug(self, base_slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project.name} - ₹{self.amount} on {self.date}"

