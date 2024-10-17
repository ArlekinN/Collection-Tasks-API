import connexion
import six

from swagger_server.models.dto_task import DTOTask  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server import util


def create_task(body=None):  # noqa: E501
    """Create a new task

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [DTOTask.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_task(id_task):  # noqa: E501
    """Delete a task

     # noqa: E501

    :param id_task: id task to be deleted
    :type id_task: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_tasks():  # noqa: E501
    """Get a task list

    Returns all tasks # noqa: E501


    :rtype: List[Task]
    """
    return 'do some magic!'


def get_task_by_id(id_task):  # noqa: E501
    """Find task by ID

    Returns a single task # noqa: E501

    :param id_task: id task to be returned
    :type id_task: str

    :rtype: Task
    """
    return 'do some magic!'


def update_task(id_task, body=None):  # noqa: E501
    """Update task

     # noqa: E501

    :param id_task: id task that need to be update
    :type id_task: str
    :param body: Update an existent task
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
