# coidng=utf-8
from appium import webdriver
from appium.webdriver.common.mobileby import By
import unittest,os,time
from app.common.Swipe_swipe import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from app.common.lxyd import Lxyd
from app.page import get_yaml
min_loc = get_yaml.MinePage()
shouye_loc = get_yaml.ShouyePage()
class Lexin(unittest.TestCase):
    def setUp(self):
        self.fz = Lxyd()
        self.dr = self.fz.lunachapp()

        self.mine_loc = (min_loc[3]['type'],min_loc[3]['value'])
        self.userinfo_loc = (min_loc[4]['type'],min_loc[4]['value'])
        self.apiname_loc = (min_loc[5]['type'],min_loc[5]['value'])
        self.srfname_loc = (min_loc[6]['type'],min_loc[6]['value'])
        self.srfconfirm_loc = (min_loc[7]['type'],min_loc[7]['value'])
        self.youyang_loc = (shouye_loc[8]['type'], shouye_loc[8]['value'])
        self.yytitle_loc = (shouye_loc[9]['type'], shouye_loc[9]['value'])
        self.ivright_loc = (shouye_loc[11]['type'], shouye_loc[11]['value'])
        # self.mubiao_loc = (shouye_loc[12]['type'], shouye_loc[12]['value'])
        self.xzmb_loc = (shouye_loc[13]['type'], shouye_loc[13]['value'])
        self.mbok_loc = (shouye_loc[14]['type'], shouye_loc[14]['value'])
        self.savemb_loc = (shouye_loc[15]['type'], shouye_loc[15]['value'])
        self.tvneed_loc = (shouye_loc[16]['type'], shouye_loc[16]['value'])
        self.tvtarget_loc = (shouye_loc[17]['type'], shouye_loc[17]['value'])
        self.yyjh_loc = (shouye_loc[18]['type'], shouye_loc[18]['value'])
        self.yyjhpass_loc = (shouye_loc[19]['type'], shouye_loc[19]['value'])
        self.yyjhtitle_loc = (shouye_loc[20]['type'], shouye_loc[20]['value'])
        self.yyjhright_loc = (shouye_loc[21]['type'], shouye_loc[21]['value'])

    def tearDown(self):
        self.dr.quit()


    def test001_updatename(self):
        """更新用户名"""
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login('19000000000', '123456')
            self.fz.tan_chuan()
        except:
            self.fz.login('19000000000', '123456')
            self.fz.tan_chuan()
        try:
            username = self.fz.test_data()['username']
            self.fz.update_name(username)
            name_txt = self.fz.get_text(self.apiname_loc)
            self.assertEqual(name_txt, username)
            print('修改用户名成功')
        except Exception as e:
            self.fz.screen_shot('updatename')
            raise Exception('修改用户名失败%s' % e)


    def test002_updateyymb(self):
        """更新有氧运动时长目标"""
        try:
            swipe_up(self.dr)
            self.fz.click(self.youyang_loc)
            text = self.fz.get_text(self.yytitle_loc)
            self.assertEqual(text, '有氧运动时长')
            self.fz.click(self.ivright_loc)
            zuobiaodanji(self.dr, 1500, 550, 1536, 2560)
            self.fz.click(self.xzmb_loc)
            swipe_up(self.dr)
            self.fz.click(self.mbok_loc)
            target = self.fz.get_text(self.tvtarget_loc)
            self.fz.click(self.savemb_loc)
            tvneed = self.fz.get_text(self.tvneed_loc)
            text = '距本周' + target + '目标还需'
            # print(text,tvneed)
            self.assertEqual(tvneed, text)
            print('修改周目标成功')
        except:
            self.fz.screen_shot('updateyymb')
            raise Exception('修改周目标失败')


    def test03_yyjh(self):
        """有氧提升计划"""
        try:
            swipe_up(self.dr)
            self.fz.click(self.yyjh_loc)
            self.fz.click(self.yyjhpass_loc)
        except TimeoutException:
            pass
        try:
            tittle = self.fz.get_text(self.yyjhtitle_loc)
            self.assertEqual(tittle, '有氧能力提升计划')
            print('进入有氧能力提升计划主页')
        except:
            self.fz.screen_shot('yyjh')
            raise Exception('进入有氧能力提升计划主页失败')







