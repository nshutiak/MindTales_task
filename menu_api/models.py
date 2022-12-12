from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class DayOfweekChoises(models.Choices):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'


class Menu(models.Model):
    content = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DayOfweekChoises.choices)

    class Meta:
        unique_together = ['restaurant', 'day_of_week']

class Employee(models.Model):
    full_name = models.CharField(max_length=100)

class VoteMenu(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE)