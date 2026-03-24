from django.db import models

# Create your models here.
class Account(models.Model):
    accno  = models.IntegerField(primary_key= True)
    cname  = models.CharField(max_length = 25)
    balance = models.FloatField()
    email = models.EmailField()

class  Transaction(models.Model):
    transaction_type = {'deposit': 'deposit', 'withdrawal': 'withdrawal'}    
    ttype = models.CharField(max_length=15, choices= transaction_type.items())
    tamt  = models.FloatField()
    accno = models.ForeignKey(Account ,on_delete= models.CASCADE)
    tdate = models.DateField()