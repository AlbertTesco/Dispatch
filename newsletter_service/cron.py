from datetime import datetime, timedelta
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from newsletter_service.models import Mailing, MailingLog


def run_mailing():
    print('Running Mailing')
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    mailing = Mailing.objects.all()
    print(mailing)
    for el in mailing:
        email_list = el.client.values_list('email', flat=True)
        print(email_list)
        if (el.send_time.time() <= current_time and
                el.send_time.date() == current_date and el.status == 'started'):
            try:
                send_mail(
                    subject=el.message_set.first().subject,
                    message=el.message_set.first().body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                )

                if el.frequency == 'daily':
                    el.send_time += timedelta(days=1)
                elif el.frequency == 'weekly':
                    el.send_time += timedelta(weeks=1)
                elif el.frequency == 'monthly':
                    el.send_time += timedelta(days=30)
                el.save()
                MailingLog.objects.create(mailing=el, status='Sent', server_response='Complete')
            except SMTPException as e:
                MailingLog.objects.create(mailing=el, status='Fail',
                                          server_response=f"Failed to send message: {str(e)}")
            except Exception as e:
                MailingLog.objects.create(mailing=el, status='Fail',
                                          server_response=f"An unexpected error occurred: {str(e)}")
