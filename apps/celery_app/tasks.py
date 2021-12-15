from celery import Celery
import celeryconfig



app = Celery('tasks', backend="rpc://", broker='redis://127.0.0.1:6379//')

# directly set configuration on the app
# app.conf.update(
#     task_serializer='json',
#     accept_coontent=['json',], # Ignore other content
#     result_serializer = 'json',
#     timezone = 'Asia/Tashkent',
#     enable_utc = True,
# )


# dedicated configuration module
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y


@app.task
def hello():
    return "hello world"