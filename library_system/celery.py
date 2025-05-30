import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "check_for_overdue_loans_daily": {
        "task": "library_system.tasks.send_reminder_emails",
        "schedule": crontab(0, 0, '*', '*', '*'),  # Every day at midnight
    },
}
