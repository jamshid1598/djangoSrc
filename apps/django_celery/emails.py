from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_feedback_email(email, message):
    context = Context({'email':email, 'message':message})
    
    email_subject = render_to_string('feedback/email/feedback_email_subject.txt', context).replace('\n', '')
    email_body = render_to_string('feedback/email/feedback_email_body.txt', context)

    email_obj = EmailMessage(
        email_subject,
        email_body,
        email,
        ['djangoSrc project (celery app)'],
        [],
        headers = {'Reaply-To: ': email}
    )
    return email_obj.send(fail_silently=False)