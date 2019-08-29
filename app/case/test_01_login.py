# coidng=utf-8
from appium import webdriver
from appium.webdriver.common.mobileby import By
import unittest, os, time
from selenium.common.exceptions import *
from app.common.Swipe_swipe import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.common.lxyd import Lxyd
from app.page import get_yaml
page_loc = get_yaml.LonginPage()
min_loc = get_yaml.MinePage()
class Lexin(unittest.TestCase):
    def setUp(self):
        self.fz = Lxyd()
        self.dr = self.fz.lunachapp()
        try:
            self.fz.always_allow()
            self.fz.tan_chuan()
            self.fz.out_login()
        except:
            pass

        self.mine_loc = (min_loc[3]['type'],min_loc[3]['value'])
        self.user_id_loc = (min_loc[8]['type'], min_loc[8]['value'])

    def tearDown(self):
        self.dr.quit()
        pass

    def test001_login_success(self):
        """正常手机号密码登陆成功"""
        try:
            self.fz.login(19000000001, 123456)
            user_id_loc = ('id', 'fm_id_tv')
            self.fz.click(self.mine_loc)
            user_id = self.fz.get_text(user_id_loc)
            self.assertEqual(user_id, 'ID:5518805')
            print('登陆成功')
        except:
            self.fz.screen_shot('test001_login_success')
            raise Exception('登陆失败')

    def test002_wx_denglu(self):
        """微信登陆成功"""
        try:
            self.fz.wx_login()
            self.fz.click(self.mine_loc)
            user_id = self.fz.get_text(self.user_id_loc)
            self.assertEqual(user_id, 'ID:5408862')
            print('登陆成功')
        except:
            self.fz.screen_shot('test002_wx_denglu')
            raise Exception('微信登陆失败')

    def test003_qq_phone(self):
        """qq绑定已注册手机号"""
        try:
            self.fz.qq_login()
            self.fz.chek_regphone('19000000000')
            self.fz.click(self.mine_loc)
            user_id = self.fz.get_text(self.user_id_loc)
            self.assertEqual(user_id, 'ID:5408862')
            print('qq绑定手机号成功')
        except:
            self.fz.screen_shot('test003_qq_phone')
            raise Exception('qq绑定手机号失败')

    """qq绑定未注册账号"""
    # def test003_qq_phone(self):
    #     try:
    #         # self.fz.always_allow()
    #         self.fz.tan_chuan()
    #         self.fz.out_login()
    #         self.fz.qq_login()
    #         self.fz.chek_phone(mobile1, '123456')
    #     except:
    #         print('未登录状态登陆')
    #         self.fz.qq_login()
    #         self.fz.chek_phone(mobile1, '123456')
    #     try:
    #         self.fz.click(self.mine_loc)
    #         user_id = self.fz.get_text(self.user_id_loc)
    #         self.assertTrue(user_id)
    #         print('qq绑定手机号成功 userid :%s' % user_id)
    #     except:
    #         print('qq绑定手机号失败')

    def test004_qq_denglu(self):
        """qq登陆成功"""
        try:
            self.fz.qq_login()
            self.fz.click(self.mine_loc)
            user_id = self.fz.get_text(self.user_id_loc)
            self.assertEqual(user_id, 'ID:5408862')
            print('登陆成功')
        except:
            self.fz.screen_shot('test004_qq_denglu')
            raise Exception('微信登陆失败')

    def test005_zhuce(self):
        """注册新账号成功"""
        try:
            mobile = self.fz.test_data()['mobile']
            self.fz.zhu_ce(mobile)
            self.fz.click(self.mine_loc)
            user_id = self.fz.get_text(self.user_id_loc)
            self.assertTrue(user_id)
            print('注册成功 userid :%s' % user_id)
        except:
            self.fz.screen_shot('test005_zhuce')
            raise Exception('注册失败')
