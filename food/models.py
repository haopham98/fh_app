from django.db import models

# Create your models here.
from accounts.models import UserProfile  # Nếu bạn dùng custom User


class Food(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        related_name='foods'
    )
    name = models.CharField(max_length=100)
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    carlories = models.FloatField()
    fiber = models.FloatField(blank=True, null=True)
    vitamin = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)