[Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/#overview)

[Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)

[Celery docs](https://docs.celeryproject.org/en/master/index.html)

[Workers Guide (celery)](https://docs.celeryproject.org/en/latest/userguide/workers.html)

[What is Redis?](https://realpython.com/caching-in-django-with-redis/#what-is-redis)

[How to Use Redis With Python?](https://realpython.com/python-redis/#installing-redis-from-source)

[installing redis-server on kali](https://installati.one/kalilinux/redis/)


[using celery with django (official docs)](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django)

[supervisord](http://supervisord.org/)

##############################
#    chack Celery worker     #
##############################

$ celery -A projectroot worker -l info




% ====================================== %
%       using RebbitMQ with Celery       %
% ====================================== %
[using RabbitMQ with Celery](https://docs.celeryproject.org/en/latest/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq)
# installing Ubuntu or Debian
$: sudo apt-get install rabbitmq-server
# run rabbitmq on docker
$: docker run -d -p 5672:5672 rabbitmq


% ====================================== %
%        using Redis with Celery         %
% ====================================== %
[Using Redis with Celery](https://docs.celeryproject.org/en/latest/getting-started/backends-and-brokers/redis.html#broker-redis)
#installing on Ubuntu or Debian
$: sudo apt-get install redis-server
# run redis on docker
$: docker run -d -p 6379:6379 redis



