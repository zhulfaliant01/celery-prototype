from scraper.tasks import scrape_task
from celery_app import app
app.send_task('scraper.scrape_task', args=[5,10])
