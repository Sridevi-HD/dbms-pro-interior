from django.db import models

# Create your models here

PAY_MODE={
    ("Credit_card","Credit_card"),
    ("Debit_card","Debit_card")

}
class Bookingdetails(models.Model):
    objects=models.Manager()
    first_name=models.CharField(max_length=20)
    user_name=models.CharField(max_length=30,primary_key=True)
    phone_no=models.BigIntegerField()
    address1=models.CharField(max_length=100)
    

    paymode=models.CharField(choices=PAY_MODE,max_length=30)
    cc_name=models.CharField(max_length=10)
    cc_number=models.IntegerField()
    cc_experation=models.CharField(max_length=20)
    cc_cvv=models.IntegerField()
