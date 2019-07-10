from django.db import models


class Category(models.Model):
    Category_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Category_Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=10)
    Price = models.CharField(max_length=5)

    Product_category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Cart(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=10)
    Price = models.CharField(max_length=5)
    Quantity = models.FloatField(max_length=2)

    def __str__(self):
        return self.Name

