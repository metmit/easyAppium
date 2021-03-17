import os

from utils import utils
from appium.webdriver.appium_service import AppiumService


class Server(object):

    @staticmethod
    def start(_serial, _port):
        # os.system("adb -s {} uninstall io.appium.android.ime".format(_serial))
        # os.system("adb -s {} uninstall io.appium.unlock".format(_serial))
        # os.system("adb -s {} uninstall io.appium.settings".format(_serial))
        # os.system("adb -s {} uninstall io.appium.uiautomator2.server".format(_serial))
        # os.system("adb -s {} uninstall io.appium.uiautomator2.server.test".format(_serial))

        bp_port = utils.valid_port(int(_port) + 2000)

        log_file = os.path.join('/tmp/appium_{}.log'.format(_serial))

        service = AppiumService()
        service.start(args=['-p', str(_port), '-bp', str(bp_port), '-U', _serial,
                            '--session-override', '--no-reset',
                            '--log-level', 'error', '--log', log_file], timeout_ms=2000)
