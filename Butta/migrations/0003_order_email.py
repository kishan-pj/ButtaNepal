# Generated by Django 4.0.1 on 2022-02-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Butta', '0002_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]