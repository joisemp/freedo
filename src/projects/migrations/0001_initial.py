# Generated by Django 4.2 on 2025-05-06 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0003_client_freelancer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_projects', to='clients.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
