from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)


class DebtAmount(models.Model):
    price = models.DecimalField(decimal_places=5, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    debtor = models.ManyToManyField(Customer, related_name='debtor')


class Debt(models.Model):
    creditor = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='creditor')
    debt_amount = models.ForeignKey(DebtAmount)