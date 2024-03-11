from django.db import models

# Create your models here.

class Message(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    date = models.DateField(null=True)
    msg = models.CharField(max_length=500)




    
