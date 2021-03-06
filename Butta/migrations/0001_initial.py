# Generated by Django 4.0.1 on 2022-02-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('visitor_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('visitor_name', models.CharField(blank=True, max_length=100)),
                ('visitor_subject', models.CharField(blank=True, max_length=100)),
                ('visitor_message', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'contact_tbl',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_first', models.CharField(blank=True, max_length=25)),
                ('customer_last', models.CharField(blank=True, max_length=25)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('customer_picture', models.FileField(blank=True, default='picture.jpg', upload_to='profile')),
                ('is_login', models.BooleanField(default=False)),
                ('review', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'customer_tbl',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, default='customer', max_length=25)),
                ('country_name', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('butta', models.FileField(blank=True, default='butta.jpg', upload_to='butta')),
            ],
            options={
                'db_table': 'order_tbl',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=50)),
                ('product_price', models.CharField(blank=True, max_length=10)),
                ('product_image', models.FileField(blank=True, default='product.jpg', upload_to='product')),
            ],
            options={
                'db_table': 'product_tbl',
            },
        ),
    ]
