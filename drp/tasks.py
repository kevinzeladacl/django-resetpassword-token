from django.core.mail import EmailMessage
from celery.decorators import task
from celery.utils.log import get_task_logger

from .tasks import *
from apps.users.models import User


logger = get_task_logger(__name__)

@task()
def send_token(msg,user_email):
	user_email = user_email
	email = EmailMessage('Reset Password', msg , to=[user_email])
	email.send()


