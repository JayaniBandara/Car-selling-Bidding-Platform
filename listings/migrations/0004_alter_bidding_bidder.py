# Generated by Django 4.0.3 on 2023-12-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_bidding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='bidder',
            field=models.CharField(max_length=100),
        ),
    ]