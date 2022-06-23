import time
from celery import shared_task

@shared_task(bind=True)
def trial_func(self): 
    print("Hota hai hota hai")
    return "kuch kuch hota hai"