from django.forms import ModelForm
from .models import Listing
from .models import Bidding


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'name',
            'description',
            'brand',
            'milage',
            'price',
            'image'
        ]

class BiddingForm(ModelForm):
    class Meta:
        model = Bidding
        fields = [
            'car_make',
            'car_model',
            'car_year',
            'image',
            'bid_Start',
            'bidder',
            'bid_amount',           
        ]

        




