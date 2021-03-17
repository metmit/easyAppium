import random
import time

from core.session import Session
from core.task import Task
from utils.config import Config
from utils.tools import AppiumTools


class Runner(object):
    def __init__(self, serial, port, app_name):
        self._serial = serial
        # 会话

        # webdriver.Remote
        self._session = Session(serial, port, Config.get_session(app_name)).get_session()

        # 处理器
        self._processor = Config.get_processor(app_name)(serial, self._session)

        # 任务生产者
        self._producer = Config.get_producer(app_name)()

        # 工具集
        self._appium_tools = AppiumTools(self._serial, self._session)

    def run(self):
        while True:
            report = []
            # 获取任务
            try:
                tasks = self._producer.get_task()
            except Exception as e:
                print("获取任务失败：{}".format(str(e)))
                break

            # 执行任务
            for task in tasks:
                time.sleep(random.random())
                if not isinstance(task, Task):
                    print("任务类型错误：[{}] {}".format(type(task), str(task)))
                    continue
                try:
                    res = self._processor.run(task)
                    if res is True:
                        self._appium_tools.press_back()
                except Exception as e:
                    report.append(task)
                    print("任务执行失败：{} {} ".format(str(task), str(e)))

            # 处理失败的任务
            self._producer.report(report)

        self.quit()  # TODO

    def quit(self):
        try:
            self._appium_tools.quit()
        except Exception as e:
            pass
