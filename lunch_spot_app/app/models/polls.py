from django.db import models
from .restaurant import Restaurant
from .employee import Employee


class Poll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee} voted for {self.restaurant} on {self.date}"
