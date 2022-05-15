import email
from django.db import models

# Create your models here.

class Register(models.Model):  
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table='register'

class AddAddress(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/')
    username=models.CharField(max_length=120)
    number=models.CharField(max_length=20)
    email_id=models.CharField(max_length=150)
    place=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    class Meta:
        db_table='add_address'

