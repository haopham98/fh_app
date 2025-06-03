from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return str(self.username)