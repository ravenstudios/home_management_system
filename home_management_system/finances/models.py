from django.db import models


# Create your models here.

class Bill(models.Model):
    name = models.CharField(max_length=255)
    ammount = models.IntegerField()
    due_date = models.IntegerField()


class Paycheck(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    ammount = models.IntegerField()
    bills = models.ManyToManyField(Bill,  blank=True)

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name
