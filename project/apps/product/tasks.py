from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta
from .report_admin import send_report
from celery.schedules import crontab

logger = get_task_logger(__name__)

@periodic_task(run_every=crontab(minute=0, hour=10))
def report():
    try:
        send_report()
    except Exception as err:
        print 'exc', err
    logger.info('OK!')
