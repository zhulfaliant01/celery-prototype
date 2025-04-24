from celery import Celery
import scraper

app = Celery('tasks', broker='redis://172.19.3.236:6379/0',
    backend='redis://172.19.3.236:6379/0')

app.autodiscover_tasks(['scraper'])