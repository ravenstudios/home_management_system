from django.db import models


# Create your models here.

class Bill(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    ammount = models.DecimalField(max_digits=6, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return self.name



class Paycheck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    ammount = models.DecimalField(max_digits=6, decimal_places=2)
    ammount_in_bank = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    bills = models.ManyToManyField(Bill, blank=True)
    bills_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    balance  = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField()

    def __str__(self):
        return self.name
