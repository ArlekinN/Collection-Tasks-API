from prometheus_client import Counter
# Счётчики запросов для разных эндпоинтов
REQUEST_COUNT_TASKS = Counter(
    'tasks_requests_total',
    'Total number of requests to /tasks endpoint',
    ['method', 'endpoint']  # метка для метода (GET, POST и т.д.)
)

REQUEST_COUNT_SECTION = Counter(
    'sections_requests_total',
    'Total number of requests to /section endpoint',
    ['method', 'endpoint']  # метка для метода (GET, POST и т.д.)
)