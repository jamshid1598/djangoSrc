broker_url='redis://127.0.0.1:6379//'
result_backend='rpc://'


task_serializer='json'
accept_coontent=['json',] # Ignore other content
result_serializer = 'json'
timezone = 'Asia/Tashkent'
enable_utc = True



task_routes = {
    "tasks.add": {"rate_limit":"20/m"},
}