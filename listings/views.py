from django.shortcuts import render
from .models import Listing
from datetime import timedelta
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    # ! get all data from listing database
    listings = Listing.objects.all()
    # ! pass database records into listings context
    context = {'listings':listings}
    return render(request, 'listings/listings.html', context )

def listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    print("*** *** listing=", listing_id, listing.address, listing.description)
    return render(request, 'listings/listing.html', {'listing':listing})

def search(request):
    return render(request, 'listings/search.html')
