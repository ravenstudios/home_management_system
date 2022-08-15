from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, default="Item")
    note = models.CharField(max_length=20, default=0, blank=True)

    def __str__(self):
        return self.name



class List(models.Model):
    # dropdown for TYPE with colors
    name = models.CharField(max_length=20, default=0)
    note = models.CharField(max_length=20, default=0, blank=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.name
