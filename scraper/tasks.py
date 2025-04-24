from celery import shared_task

@shared_task(name="scraper.scrape_task")
def scrape_task(a, b):
    return a + b