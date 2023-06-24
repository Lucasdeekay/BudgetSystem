from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    username = models.CharField(max_length=25)
    email = models.EmailField()


class Expense(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())


class Budget(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.ManyToManyField(Expense)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())
