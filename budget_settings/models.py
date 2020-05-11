from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BankAccount(models.Model):
    Name = models.CharField(max_length=50)
    Comment = models.TextField(blank=True)

    def __str__(self):
        return self.Name


class TransactionType(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Transaction(models.Model):
    Date = models.DateField()
    TransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, verbose_name='Transaction Type')
    BankAccount = models.ForeignKey(BankAccount, on_delete=models.CASCADE, verbose_name='Bank Account')
    Image = models.ImageField(upload_to='media/transaction_img')
    Amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.Date