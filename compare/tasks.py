from celery import shared_task

@shared_task(bind=True)
def func(self): 
    print(1)
    return "ho gya"