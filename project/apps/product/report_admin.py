from django.core.mail import send_mail
from django.utils import timezone

from .models import ProductLikes, ProductComments


def send_report():
    day_before = timezone.now() - timezone.timedelta(days=1)
    likec_c = ProductLikes.objects.filter(created_at__gte=day_before).count()
    comments_c = ProductComments.objects.filter(created_at__gte=day_before).count()

    subject = 'Daily report from site'
    message = 'From {} to {} you got {} likes and {} comments'.format(
        day_before.strftime("%Y-%m-%d %H:%M"),
        timezone.now().strftime("%Y-%m-%d %H:%M"),
        likec_c,
        comments_c
    )
    from_email = 'mail@gmail.com'
    to_mail = ['admin@gmail.com']
    # if subject and message:
    #     try:
    send_mail(subject, message, from_email, to_mail)
        # except Exception as err:
        #     print Exception
