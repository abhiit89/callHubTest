from django.db import models

# Create your models here.
class Fibonacci(models.Model):
    index = models.BigIntegerField(default=None)
    result = models.BigIntegerField(default=None)