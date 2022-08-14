from django.db import models


class Bill(models.Model):
    name = models.CharField(max_length=20, default="BILL")
    ammount = models.DecimalField(max_digits=6, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Paycheck(models.Model):
    name = models.CharField(max_length=20, default=0)
    ammount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    ammount_in_bank = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    bills = models.ManyToManyField(Bill, blank=True)
    # bills = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bills', null=True, blank=True)

    bills_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    balance  = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField()

    def __str__(self):
        return self.name
