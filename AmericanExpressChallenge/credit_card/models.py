from django.db import models

# Create your models here.
class credit_card_details(models.Model):
    user_id=models.IntegerField()
    name=models.CharField(max_length=200)
    limit_bal = models.FloatField()
    sex=models.IntegerField()
    education=models.IntegerField()
    marriage=models.IntegerField()
    age=models.IntegerField()
    pay_0=models.IntegerField()
    pay_2=models.IntegerField()
    pay_3=models.IntegerField()
    pay_4=models.IntegerField()
    pay_5=models.IntegerField()
    pay_6=models.IntegerField()
    bill_amt_1=models.FloatField()
    bill_amt_2=models.FloatField()
    bill_amt_3=models.FloatField()
    bill_amt_4=models.FloatField()
    bill_amt_5=models.FloatField()
    bill_amt_6=models.FloatField()