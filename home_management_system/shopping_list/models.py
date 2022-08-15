from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, default="Item")
    note = models.TextField(blank = True)
    date = models.DateField()

    def __str__(self):
        return self.name



class List(models.Model):
    # dropdown for TYPE with colors
    name = models.CharField(max_length=20, default=0)
    note = models.TextField(blank = True)
    items = models.ManyToManyField(Item, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name
