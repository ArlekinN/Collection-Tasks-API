from prometheus_client import Counter
REQUEST_COUNT = Counter(
    'task_requests_total',
    'Total number of requests to tasks endpoints',
    ['method', 'endpoint']
)