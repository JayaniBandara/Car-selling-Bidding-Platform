# Generated by Django 4.0.3 on 2023-12-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rename_bid_start_bidding_bid_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='bidder',
            field=models.EmailField(max_length=100),
        ),
    ]