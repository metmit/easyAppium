import time
from multiprocessing import Process
from core.server import Server as AppiumServer
from core.runner import Runner
from utils import utils


class Start(object):

    def __init__(self, serial, port, app_name):
        self._port = port
        self._serial = serial
        self._app_name = app_name

    @staticmethod
    def server(serial, port):
        AppiumServer().start(serial, port)

    @staticmethod
    def client(serial, port, app_name):
        Runner(serial, port, app_name).run()

    def run(self):

        try:
            processes = {}

            print("准备启动：{}".format(self._serial))

            # 杀死相关进程
            utils.kill_process(self._serial)

            # 检查可用的端口号
            self._port = utils.valid_port(self._port)

            # appium-server
            p = Process(target=self.server, args=(self._serial, self._port), name='server_' + self._serial)
            p.start()
            processes[str(p.pid)] = {'serial': self._serial, 'process': p, 'pid': str(p.pid), 'type': 'server'}
            p.join(10)

            # appium client & runner
            p = Process(target=self.client, args=(self._serial, self._port, self._app_name),
                        name='client_' + self._serial)
            p.start()
            processes[str(p.pid)] = {'serial': self._serial, 'process': p, 'pid': str(p.pid), 'type': 'client'}
            time.sleep(5)
            # p.join(5)

            print("启动完成：{}".format(self._serial))
            return processes

        except Exception as e:
            print("启动错误：[{}] {}".format(self._serial, str(e)))
            utils.kill_process(self._serial)


if __name__ == '__main__':
    _processes = Start("acfed153d1s", 4723, "gifmaker").run()
    print(_processes)
