# coidng=utf-8
import os, time
from macaca import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from app.common.Swipe_swipe import *
from app.page import get_yaml
page_loc = get_yaml.LonginPage()
min_loc = get_yaml.MinePage()
zhuce_loc = get_yaml.ZhucePage()
class Fengzhuang(object):
    def lunachapp(self):
        desired_caps = {
            'platformName': 'Desktop',
            'browserName' : 'Chrome'
        }

        self.dr = WebDriver(desired_caps)
        time.sleep(3)
        return self.dr

    def find_element(self, locator, timeout=3):
        element = WebDriverWait(self.dr, timeout, 0.5).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator,timeout=3):
        elements = WebDriverWait(self.dr, timeout, 0.5).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def clear_key(self, locator):
        element = self.find_element(locator)
        element.clear()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        element = self.find_element(locator)
        return element.text


    def tan_chuan(self):
        ivclose_loc = ('id', 'gz.lifesense.weidong.qa:id/ivDialogClose')
        try:
            self.dr.wait_activity('gz.lifesense.weidong.ui.activity.main.MainActivityNew', 1)
            self.click(ivclose_loc)
            print('首页弹窗已关闭')
        except:
            pass

    def always_allow(self, number=3):
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(self.dr, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def is_toast_exist(self, text, timeout=2, poll_frequency=0.1):
        try:
            toast_loc = ('xpath', "//*[contains(@text,'%s')]" % text)
            if WebDriverWait(self.dr, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc)):
                return True
        except:
            return False

    def screen_shot(self, text):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        img_path = os.path.join(base_path, 'report\\img\\')
        # print(img_path)
        times = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_save_path = img_path + times + text + '.png'
        # print(screen_save_path)
        self.dr.get_screenshot_as_file(screen_save_path)


if __name__ == '__main__':
    a = Fengzhuang()
    dr = a.lunachapp()
    dr.init()
    dr.get('http://www.baidu.com')
    a.send_keys(('id', 'kw'), 'macaca')
    a.click(('id', 'su'))
    dr.close()
