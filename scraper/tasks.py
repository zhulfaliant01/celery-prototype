from celery import shared_task
import time

@shared_task(name="scraper.scrape_task")
def scrape_task(a, b):
    time.sleep(15)
    return a + b