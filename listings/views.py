from django.shortcuts import render
from .models import Listing


# Create your views here.


def index(request):
    # return render(request, 'listings/listings.jinja2', {
    #     'name': 'Machado'
    # })
    listings = Listing.objects.all()        # find data's in postgresql
    context = {
        "listings": listings
    }
    return render(request, 'listings/listings.jinja2', context)


def listing(request, listing_id):
    print(listing_id)
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
