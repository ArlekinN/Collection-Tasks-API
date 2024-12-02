from swagger_server.metrics import REQUEST_COUNT_SECTION

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
    # Увеличиваем счетчик запросов
    REQUEST_COUNT_SECTION.labels(method='GET', endpoint='/section').inc()

    # Возвращаем задачи
    return sections, 200
