# Generated by Django 3.0.5 on 2020-05-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_auto_20200513_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='paymode',
            field=models.CharField(choices=[('Credit_card', 'Credit_card'), ('Debit_card', 'Debit_card')], max_length=30),
        ),
    ]
