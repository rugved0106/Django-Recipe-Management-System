from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipies(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name_r = models.CharField(max_length=100)
    dis_r = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/')


