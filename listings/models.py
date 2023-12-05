from django.db import models
from django.contrib.auth.models import User



class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    milage = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()

def __str__(self):
        return f"{self.name} <br> {self.brand} ({self.mileage} miles) <br> ${self.price} <br> Image: {self.image} <br> Description:{self.description} "
    

class Bidding(models.Model):
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.PositiveIntegerField()
    bidder = models.EmailField(max_length=100) 
    bid_Start = models.DecimalField(max_digits=10, decimal_places=2)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

    def _str_(self):
        return f"Bid #{self.id} <br> on {self.car_make} {self.car_model} <br> by {self.bidder} <br> for LKR{self.bid_amount} <br> {self.image.name}" 