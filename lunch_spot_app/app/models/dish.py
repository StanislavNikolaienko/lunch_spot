from django.db import models
from .menu import Menu


class Dish(models.Model):
    menus = models.ManyToManyField(Menu)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.description} for {self.price}"
