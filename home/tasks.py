import time
from celery import shared_task

@shared_task(bind=True)
def getData(self): 
    print("Task Completed")
    return "some data"