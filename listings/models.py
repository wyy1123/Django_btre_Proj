from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    #on_delete specifies that if realtor gets deleted the listing doenst get deleted
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zipcode= models.CharField(max_length=20)
    #blank specifies that we dont require this to be filled
    #textfield doenst need to specify length
    description= models.TextField(blank=True)
    price= models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    # we want to  specify where in the media folder we want the photo to be uploaded
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    #this is the field that'll be displayed in the admin area
    def __str__(self):
        return self.title






