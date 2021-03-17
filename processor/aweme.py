import json
import random
import time

from core.processor import Processor


class AwemeProcessor(Processor):

    def __init__(self, serial, _session):
        super().__init__(serial, _session)

    def run(self, task):

        self.log("任务：" + json.dumps(task))

        if task.get_action() == 'feed':
            return self.feed()

        if task.get_action() == 'profile':
            return self.kol_detail(task.get_params('uid'))

    def feed(self):
        url = 'snssdk1128://feed?refer=web'
        self._session.get(url)

        x = self._session.get_window_size()['width']
        y = self._session.get_window_size()['height']

        for i in range(10):
            try:
                time.sleep(1 + float(random.random()))
                self._session.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.2), 700)
            except Exception as e:
                self.log("swipe失败：" + str(e))
                break

        return True

    def kol_detail(self, uid):
        url = "snssdk1128://user/profile/{}?refer=web&gd_label=click_wap_profile_bottom&type=need_follow&needlaunchlog=1"
        self._session.get(url.format(uid))
        time.sleep(5)
        return True
