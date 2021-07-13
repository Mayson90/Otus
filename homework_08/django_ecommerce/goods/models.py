from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=15)
    img = models.ImageField(upload_to='vendors', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()
    img = models.ImageField(upload_to='goods', blank=True, null=True)

    def __str__(self):
        return self.name
