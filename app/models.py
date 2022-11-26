from django.db import models
from core.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)


class Debt(models.Model):
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creditor')
    date = models.DateTimeField(auto_now_add=True)


class DebtAmount(models.Model):
    price = models.DecimalField(decimal_places=5, max_digits=10)
    debtor = models.ForeignKey(User, related_name='debtor', on_delete=models.CASCADE)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
