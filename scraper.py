from celery import shared_task

@shared_task(name='scraper')
async def scrape_task(x, y):
    return x + y