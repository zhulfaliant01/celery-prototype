from celery import Celery
import scraper

app = Celery('tasks', broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0')

app.autodiscover_tasks(['scraper'])