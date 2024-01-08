from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class BudgetUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name}, {self.email}'


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Budget(models.Model):

    BUDGET_CHOICES = {
        "Income": 'Income',
        'Expense': 'Expense',
    }

    MONTH = {
        'Jan': 'January',
        'Feb': 'February',
        'Mar': 'March',
        'Apr': 'April',
        'May': 'May',
        'June': 'June',
        'July': 'July',
        'Aug': 'August',
        'Sep': 'September',
        'Oct': 'October',
        'Nov': 'November',
        'Dec': 'December'
    }

    user = models.ForeignKey(BudgetUser, on_delete=models.CASCADE, related_name='budget', default=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    budget_choice = models.CharField(max_length=10, choices=BUDGET_CHOICES, default='Expense')
    date = models.DateField(auto_now_add=True)
    month = models.CharField(max_length=20, choices=MONTH, default='Jan')

    def __str__(self):
        return self.name















