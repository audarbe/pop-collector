from django.db import models

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=100)
    serial = models.IntegerField()
    details = models.TextField(max_length=300)
    category = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name