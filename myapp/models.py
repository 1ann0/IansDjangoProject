from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return self.firstname + " " + self.lastname

class Product(models.Model):
    productid = models.IntegerField(default=0)
    productname = models.CharField(max_length=50)
    productquantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.productname
