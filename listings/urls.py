from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='listings'),
#/listings/23 will be the address for a single listing. so we need to include a parameter
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search'),

]