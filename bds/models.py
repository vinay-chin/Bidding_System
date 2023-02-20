from django.db import models

class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField( max_length=30,primary_key=True)
    password = models.CharField(max_length=20)

class form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=30,primary_key=True)
    phno = models.BigIntegerField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name

