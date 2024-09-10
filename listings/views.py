from django.shortcuts import render
from .models import Listing
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

# Create your views here.
def index(request):
    # ! get all data from listing database
    #listings = Listing.objects.all().order_by('list_date')
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # ! pass database records into listings context
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context )

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    # print("*** *** listing=", listing_id, listing.address, listing.description)
    return render(request, 'listings/listing.html', {'listing':listing})

def search(request):
    return render(request, 'listings/search.html')
