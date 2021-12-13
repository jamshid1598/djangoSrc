# from celery.decorators import task
# from celery.utils.log import get_task_logger
# from .emails import send_feedback_email


# logger = get_task_logger(__name__)


# @task(name="send_feedback_email_task")
# def send_feedback_email_task(email, message):
#     """sends an email when feedback form is filled successfully"""
#     logger("send email successfully")
#     return send_feedback_email(email, message)





from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379//')

@app.task
def add(x, y):
    return x + y