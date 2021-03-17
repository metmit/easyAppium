from core.session import Session
from utils.config import Config
from appium import webdriver


class StartSession(object):

    def __init__(self, serial="", port=4723, platform=""):
        self._port = port
        self._serial = serial
        config = Config.get_session(platform)
        self.session = Session(serial, port, config).get_session()

    def get_session(self) -> webdriver.Remote:
        return self.session


if __name__ == '__main__':
    StartSession(serial="123123", port=4723)
