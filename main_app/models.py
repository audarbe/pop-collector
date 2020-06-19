from django.db import models
from django.urls import reverse

VARIANTS = (
    ('ST', 'Standard'),
    ('MT', 'Metallic'),
    ('FL', 'Flocked'),
    ('GD', 'Glow In The Dark'),
    ('BW', 'Black and White'),
    ('PT', 'Patina'),
    ('OF', 'Outfits'),
    ('CW', 'Colorways'),
    ('PR', 'Proto'),
)

# Create your models here.
class Accessory(models.Model):
  name = models.CharField(
      max_length=50,
      null=True,
      )
  color = models.CharField(
      max_length=20,
      null=True,
      )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pops', kwargs={'pk': self.id})

class Pop(models.Model):
    name = models.CharField(max_length=100)
    serial = models.IntegerField()
    details = models.TextField(max_length=300)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pops_detail', kwargs={'pk': self.id})

class Limited(models.Model):
    name = models.CharField(max_length=100)
    typeOfVariant = models.CharField(
        max_length=2,
        choices=VARIANTS,
        default=VARIANTS[0][0],
        verbose_name='Type of Variant'
        )
    pop = models.ForeignKey(Pop, on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.get_typeOfVariant_display()} - {self.name}"