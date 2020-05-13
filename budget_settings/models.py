from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Name


class Account(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Comment = models.TextField(blank=True)

    def __str__(self):
        return self.Name


def increment_transaction_number():
    last_number = Transaction.objects.all().order_by('id').last()
    if not last_number:
        return 'TR00001'
    invoice_no = last_number.Number
    invoice_int = int(invoice_no.split('TR')[-1])
    width = 5
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'TR' + str(formatted)
    return new_invoice_no


class Transaction(models.Model):
    Date = models.DateField(blank=True)
    Number = models.CharField(max_length=500, default=increment_transaction_number, null=True, blank=True)
    Withdrawal = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    Deposit = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Bank Account')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category Account')
    Image = models.ImageField(upload_to='media/transaction_img', blank=True, null=True)
    Amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.Number
