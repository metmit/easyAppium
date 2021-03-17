from core.server import Server as AppiumServer


class StartServer(object):

    def __init__(self, serial="", port=4723):
        self._port = port
        self._serial = serial
        AppiumServer().start(serial, port)


if __name__ == '__main__':
    StartServer(serial="123123", port=4723)
