
from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    
    restaurant = Restaurant()
    restaurant.name = "My Italian Restaurant #2"
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    restaurant.latitude = 50.2
    restaurant.longitude =  50.5
    restaurant.save()
   
    print(connection.queries)