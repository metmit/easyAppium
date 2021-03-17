import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from appium import webdriver
from selenium.webdriver.common.by import By


class AppiumTools(object):
    __instance = None

    def __init__(self, serial: str, session: webdriver.Remote):
        self._session = session
        self.serial = serial
        self.x = self._session.get_window_size()['width']
        self.y = self._session.get_window_size()['height']
        self.byTypes = {
            "id": By.ID,
            "xpath": By.XPATH,
            "name": By.NAME,
            "tag": By.TAG_NAME,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "link": By.LINK_TEXT,
            "partial": By.PARTIAL_LINK_TEXT,
        }

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def destruct(self):
        self.__instance = None

    def quit(self):
        self._session.quit()
        self.destruct()

    # 根据屏幕比例进行滑动
    def swipe(self, ratio_x1, ratio_y1, ratio_x2, ratio_y2, duration):
        self._session.swipe(ratio_x1 * self.x, ratio_y1 * self.y, ratio_x2 * self.x, ratio_y2 * self.y, duration)

    # 按下返回键
    def press_back(self, sleep=0.1):
        self._session.keyevent(4)
        time.sleep(sleep)

    # 判断textview是否存在
    def is_textview_exists(self, text, timeout: float = 1):
        return self.get_element('xpath', "//android.widget.TextView[@text='%s']" % text, timeout)

    # 判断toast弹窗是否存在
    def is_toast_exists(self, text, timeout: float = 1):
        e = self.get_element('xpath', ".//*[contains(@text,'%s')]" % text, timeout)
        if e is False:
            return False
        return text in e.text

    # 判断元素是否存在
    def get_element(self, byType, selector, timeout: float = 1):
        if byType not in self.byTypes:
            raise Exception("元素类型错误")
        try:
            wait = WebDriverWait(self._session, timeout, 0.2, ElementNotVisibleException)
            return wait.until(EC.presence_of_element_located((self.byTypes[byType], selector)))
        except Exception as e:
            return False

    # 判断元素是否可点击
    def is_element_clickable(self, byType, selector, timeout=1):
        if byType not in self.byTypes:
            raise Exception("元素类型错误")
        try:
            wait = WebDriverWait(self._session, timeout, 0.2, ElementNotVisibleException)
            return wait.until(EC.element_to_be_clickable((self.byTypes[byType], selector)))
        except Exception as e:
            return False

    # 判断元素是否出现在当前页面
    def is_element_displayed(self, byType, selector, y_ratio, timeout=3):
        if byType not in self.byTypes:
            raise Exception("元素类型错误")
        try:
            wait = WebDriverWait(self._session, timeout, 0.2, ElementNotVisibleException)
            el = wait.until(EC.visibility_of_element_located((self.byTypes[byType], selector)))
            loc = el.location_once_scrolled_into_view
            if loc and loc['y'] < y_ratio * self.y:
                return el
            else:
                return False
        except Exception as e:
            return False

    # 根据ID点击元素
    def click_element_by_id(self, selector, timeout=1):
        return self.click_element('id', selector, timeout)

    # 根据text点击元素
    def click_element_by_textview(self, text, timeout=0.2):
        return self.click_element('xpath', "//android.widget.TextView[@text='%s']" % text, timeout)

    # 点击包含（text）元素
    def click_element_by_contain_textview(self, text, timeout=0.2):
        return self.click_element('xpath', ".//*[contains(@text,'%s')]" % text, timeout)

    # 点击元素
    def click_element(self, byType, selector, timeout: float = 1):
        try:
            ele = self.get_element(byType, selector, timeout)
            if ele is False:
                return False
            ele.click()
            return True
        except Exception as e:
            return False

    # 根据位置点击元素
    def click_element_by_location(self, x, y):
        try:
            self._session.tap([(x, y)], 100)
            return True
        except Exception as e:
            return False

    # 根据内容描述来点击元素
    def click_element_by_content_desc(self, content):
        try:
            self._session.find_element_by_accessibility_id(content).click()
            return True
        except Exception as e:
            return False
