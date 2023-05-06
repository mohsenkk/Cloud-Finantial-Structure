import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloudFinantialStructure.settings")
app = Celery("cloudFinantialStructure")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-30-seconds': {
        'task': 'apis.tasks.invoice_creator',
        'schedule': 30,
    },
}
app.conf.timezone = 'UTC'