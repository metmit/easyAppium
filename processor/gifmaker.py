import json
import time

from core.processor import Processor


class GifMakerProcessor(Processor):

    def __init__(self, serial, _session):
        super().__init__(serial, _session)

    def run(self, task):
        self.log("任务：" + json.dumps(task))

        if task.get_action() == 'profile':
            return self.kol_detail(task.get_params('uid'))

        if task.get_action() == 'search':
            return self.search(task.get_params('keyword'))

        return False

    def kol_detail(self, uid):
        url = "kwai://profile/{}"
        self._session.get(url.format(uid))
        time.sleep(5)
        return True

    def search(self, keyword):
        url = 'snssdk1128://search?keyword={}&display_keyword={}&enter_from=push'
        self._session.get(url.format(keyword, keyword))
        time.sleep(1)

        self._appium_tools.click_element_by_textview("用户")
        time.sleep(2)

        if self._appium_tools.is_textview_exists("您今日的搜索次数已达上限"):
            raise Exception("您今日的搜索次数已达上限")

        if self._appium_tools.is_textview_exists("请登录后重试"):
            raise Exception("请登录后重试")

        if self._appium_tools.is_textview_exists("登录后可体验完整搜索功能"):
            raise Exception("登录后可体验完整搜索功能")

        return True
