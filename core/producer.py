import abc


class Producer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._run_count = 0
        self._max_count = -1

    def get_task(self) -> list:
        self._run_count += 1

        if 0 < self._max_count < self._run_count:
            raise Exception("最大执行次数：{}".format(self._max_count))

        return self._get_task()

    @abc.abstractmethod
    def _get_task(self) -> list:
        pass

    def report(self, tasks: list):
        pass