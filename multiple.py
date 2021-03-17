import time
from start import Start
from utils import utils


class Main(object):

    def __init__(self, app_name=""):
        self.app_name = app_name

    # TODO 写死、adb、自定义配置 皆可
    def get_device(self):
        return [
            "aaadf123123",
            "ddfvffsdfsd"
        ]

    def run(self):
        try:
            processes = {}

            while True:
                _port = 4723

                devices = self.get_device()

                for serial in devices:
                    if serial in processes:
                        continue
                    _port = utils.valid_port(_port)
                    processes[str(serial)] = Start(serial, _port, self.app_name)
                    _port += 1

                time.sleep(10)
                processes = self.check_process(processes)
        except Exception as e:
            print("启动错误 {}".format(str(e)))

    @staticmethod
    def check_process(processes):
        time.sleep(5)

        serials = []

        for serial in processes.keys():
            process = processes[serial]
            clear = False
            for p in process.values():
                try:
                    if not p['process'].is_alive():  # and p['type'] == 'client'
                        clear = True
                except:
                    clear = True

            if clear:
                serials.append(serial)
                for p in process.values():
                    try:
                        p['process'].terminate()
                        p['process'].kill()
                        p['process'].close()
                        # del_list.append(p['pid'])
                    except:
                        pass

        for serial in serials:
            del processes[serial]
            utils.kill_process(serial)

        return processes


if __name__ == '__main__':
    Main().run()
