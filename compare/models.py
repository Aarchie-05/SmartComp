from django.db import models

# Create your models here.

class FlipkartDeals:
    id : int
    company : str
    title : str
    price : str 
    mrp : str  
    discount : str  
    assured : bool  
    img : str 
    item_link : str  
    rating: str 
    no_of_rating: str
    