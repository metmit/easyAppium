import abc

from appium import webdriver

from core.task import Task
from utils.tools import AppiumTools


class Processor(metaclass=abc.ABCMeta):

    def __init__(self, serial, _session: webdriver.Remote):
        self._serial = serial
        self._session = _session
        self._appium_tools = AppiumTools(self._serial, self._session)

    @abc.abstractmethod
    def run(self, task: Task):
        pass

    def log(self, message):
        print("{}: {}".format(self._serial, message))

    def swipe(self):
        pass
