from prometheus_client import Counter

REQUEST_COUNT_TASKS = Counter(
    'tasks_requests_total',
    'Total number of requests to /tasks endpoint',
    ['method', 'endpoint']
)

REQUEST_COUNT_SECTION = Counter(
    'sections_requests_total',
    'Total number of requests to /section endpoint',
    ['method', 'endpoint']
)
