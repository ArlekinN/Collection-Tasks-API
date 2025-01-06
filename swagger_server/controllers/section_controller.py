from swagger_server.metrics import REQUEST_COUNT_SECTION
from prometheus_client import Counter
from flask import jsonify

sections = [
    {
        "id": "1",
        "name": "Математика",
    },
    {
        "id": "2",
        "name": "Химия",
    }
]

def get_all_sections():
    REQUEST_COUNT_SECTION.labels(method='GET', endpoint='/sections').inc()
    return jsonify(sections), 200
