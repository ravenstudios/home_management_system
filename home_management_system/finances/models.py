from django.db import models


# Create your models here.

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ammount = models.IntegerField()
    due_date = models.DateField()
    def __str__(self):
        return self.name



class Paycheck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ammount = models.IntegerField(null=True)
    ammount_in_bank = models.IntegerField(null=True)
    bills = models.ManyToManyField(Bill, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name
