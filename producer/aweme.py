from core.task import Task
from core.producer import Producer


class AwemeProducer(Producer):

    def __init__(self):
        super().__init__()

    def _get_task(self) -> list:
        # todo demo
        action = "profile"
        params = {
            "uid": "104255897823"
        }
        task = [
            Task(action, params)
        ]
        return task
