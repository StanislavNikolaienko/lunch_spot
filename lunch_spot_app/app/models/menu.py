from django.db import models
from .restaurant import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = ("restaurant", "date")

    def __str__(self):
        return f"{self.restaurant} on {self.date}"
