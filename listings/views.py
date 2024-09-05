from django.shortcuts import render
from .models import Listing
from datetime import timedelta
from django.utils import timezone
# Create your views here.
def index(request):
    # ! get all data from listing database
    listings = Listing.objects.all()
    # ! pass database records into listings context
    context = {'listings':listings, 'date': timezone.now()}
    return render(request, 'listings/listings.html', context )

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
