from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.models import User

class Category(TextChoices):
    ComputerEngineer = 'CE', 'Computer engineer'
    ElectronicsEngineer = 'EE', 'Electronics engineer'
    Accountant = 'AC', 'Accountant'
    Secretary = 'SE', 'Secretary'


class Position(models.Model):
    title = models.CharField(max_length=100, null=False)
    valid_date = models.DateField(null=False)
    working_hours = models.PositiveIntegerField(null=False)
    salary = models.PositiveIntegerField(null=False)
    image = models.ImageField(upload_to='position/%Y/%m/%d/', null=True)
    category = models.TextField(choices=Category.choices, default=Category.ComputerEngineer, max_length=2, null=False)
    employer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    employee = models.ManyToManyField(to=User, related_name="employee")



    @property
    def employer_name(self):
        return self.employer.username

    def __str__(self):
        return self.title
