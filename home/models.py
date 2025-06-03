from django.db import models

# SQL schema i.e. how the data will be structured is defined here

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)  # added max_length
    email = models.EmailField( unique=True)  # added unique=True
    phone = models.BigIntegerField()  # changed and removed max_length


#to interact with the pythons database we use topic called shell......

class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()