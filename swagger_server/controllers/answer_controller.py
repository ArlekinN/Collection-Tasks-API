import connexion
import six

from swagger_server.models.answer_task import AnswerTask  # noqa: E501
from swagger_server import util


def get_answer_to_task_by_id(id_task):  # noqa: E501
    """Find answer to task by ID

    Returns answer to task # noqa: E501

    :param id_task: id task whose response is returned
    :type id_task: str

    :rtype: AnswerTask
    """
    return 'do some magic!'


def send_answer(body=None):  # noqa: E501
    """Send verification response

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [AnswerTask.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def update_task_answer(id_task, body=None):  # noqa: E501
    """Update task answer

     # noqa: E501

    :param id_task: id task whose answer needs to be updated
    :type id_task: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AnswerTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
