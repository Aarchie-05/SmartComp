import time
from celery import shared_task

@shared_task(bind=True)
def amazon_best_deals(self): 
    print("Task Completed")
    return "some data"