from core.task import Task
from core.producer import Producer


class GifMakerProducer(Producer):

    def __init__(self):
        super().__init__()

    def _get_task(self) -> list:
        # todo demo
        action = "profile"
        params = {
            "uid": "11131231"
        }
        task = [
            Task(action, params)
        ]
        return task
