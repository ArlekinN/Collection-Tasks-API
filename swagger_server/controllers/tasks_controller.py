import connexion
from swagger_server.models.dto_task import DTOTask
from swagger_server.models.task import Task 
from swagger_server.metrics import REQUEST_COUNT_TASKS
from flask import jsonify


def create_task(body=None):  
    """Create a new task

     # noqa: E501

    :param body:
    :type body: list | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_task(id_task): 
    """Delete a task

     # noqa: E501

    :param id_task: id task to be deleted
    :type id_task: str

    :rtype: None
    """
    return 'do some magic!'


def get_task_by_id(id_task):  
    """Find task by ID

    Returns a single task # noqa: E501

    :param id_task: id task to be returned
    :type id_task: str

    :rtype: Task
    """
    return 'do some magic!'


def update_task(id_task, body=None):  
    """Update task

     # noqa: E501

    :param id_task: id task that need to be update
    :type id_task: str
    :param body: Update an existent task
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


tasks = [
    {
        "id": "1",
        "name": "Семь колец",
        "section": {
            "id": "1",
            "name": "математика"
        },
        "complexity": "very easy",
        "description": "описание задачи"
    },
    {
        "id": "2",
        "name": "Математическая головоломка",
        "section": {
            "id": "1",
            "name": "математика"
        },
        "complexity": "easy",
        "description": "Задача средней сложности"
    },
]


def get_all_tasks():
    REQUEST_COUNT_TASKS.labels(method='GET', endpoint='/tasks').inc()
    return jsonify(tasks), 200
