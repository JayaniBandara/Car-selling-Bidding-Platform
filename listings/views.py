from django.shortcuts import redirect, render
from .models import Listing, Bidding
from .forms import ListingForm, BiddingForm
from django.http import HttpResponse

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render (request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'login.html')
    
def LogoutPage(request):
        logout(request)
        return redirect('login')
    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        else:







# views.py

from django.shortcuts import render
from .models import Bidding

def bid_update(request):
    # Retrieve the previous bid, current bid, and bid update count
    previous_bid = Bidding.objects.last()  # Assuming you have a suitable way to determine the "previous" bid
    current_bid = Bidding.objects.latest('id')  # Assuming the bids have an ID field
    bid_update_count = Bidding.objects.count()

    return render(request, 'bidupdate.html', {'form': BiddingForm(), 'previous_bid': previous_bid, 'current_bid': current_bid, 'bid_update_count': bid_update_count})



def listing(request, id):
    listing_obj = Listing.objects.get(id=id)
    context = {'listing': listing_obj}
    return render(request, 'listing.html', context)

def create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create.html', context)

def update(request, id):
    listing_obj = Listing.objects.get(id=id)
    form = ListingForm(instance=listing_obj)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing_obj)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = {'form': form}
    return render(request, 'update.html', context)

def delete(request, id):
    listing_obj = Listing.objects.get(id=id)
    listing_obj.delete()
    return redirect('/')



from .models import Listing, Bidding

def listings(request):
    listings_obj = Listing.objects.all()
    bidding_obj = Bidding.objects.all()
    
    context = {
        'listings': listings_obj,
        'biddings': bidding_obj,
    }
    
    return render(request, 'listings.html', context)


def bidding(request, id):
    bidding_obj = Bidding.objects.get(id=id)
    context = {'bidding': bidding_obj}
    return render(request, 'bidding.html', context)


def create_bid(request):
    form = BiddingForm()
    if request.method == 'POST':
        form = BiddingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'bidform.html', context)

def bid_update(request, id):
    bidding_obj = Bidding.objects.get(id=id)
    form = BiddingForm(instance=bidding_obj)
    if request.method == 'POST':
        form = BiddingForm(request.POST, request.FILES, instance=bidding_obj)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = {'form': form}
    return render(request, 'update.html', context)

def index(request):
    return render(request, 'index.html')

def webpage2(request):
    return render(request, 'about.html')

def webpage3(request):
    return render(request, 'service.html')




def webpage7(request):
    return render(request, 'team.html')



def webpage9(request):
    return render(request, 'contact.html')





