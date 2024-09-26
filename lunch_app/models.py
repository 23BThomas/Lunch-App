from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    meals_taken = models.PositiveIntegerField(default=0)
    meals_remaining = models.PositiveIntegerField(default=0)
    
class Lunch(models.Model):
    balance = models.IntegerField()
    redeemed = models.CharField(max_length=255)

    class Meta:
        app_label = 'lunch_app'

    def __str__(self):
        return f"Balance: {self.balance}, Redeemed: {self.redeemed}"