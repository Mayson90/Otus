from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
