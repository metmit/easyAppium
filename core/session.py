import os

from appium import webdriver


class Session(object):
    _session = None

    def __init__(self, serial, appium_port, config):
        self._serial = serial
        self._appium_port = appium_port
        self._config = config

        platform_version_out = os.popen('adb -s ' + serial + ' shell getprop ro.build.version.release')
        platform_version = platform_version_out.readline().strip()
        platform_version_out.close()

        # system_port = 8200 + int(appium_port) - 4723

        self._config['udid'] = serial
        self._config['deviceName'] = serial
        self._config['platformVersion'] = platform_version
        # self._config['systemPort'] = system_port

    def get_session(self) -> webdriver.Remote:
        if self._session is not None:
            return self._session

        remote = 'http://127.0.0.1:{}/wd/hub'.format(self._appium_port)

        self._session = webdriver.Remote(remote, desired_capabilities=self._config)

        return self._session
