# coidng=utf-8
from app.page import get_yaml
from app.common.Swipe_swipe import *
from app.common.fengzhuang import Fengzhuang
import yaml, os

page_loc = get_yaml.LonginPage()
min_loc = get_yaml.MinePage()
zhuce_loc = get_yaml.ZhucePage()
class Lxyd(Fengzhuang):
    def __init__(self):
        self.login_loc = (page_loc[0]['type'], page_loc[0]['value'])
        self.userphone_loc = (page_loc[1]['type'], page_loc[1]['value'])
        self.password_loc = (page_loc[2]['type'], page_loc[2]['value'])
        self.userlogin_loc = (page_loc[3]['type'], page_loc[3]['value'])
        self.shezhi_loc = (min_loc[0]['type'],min_loc[0]['value'])
        self.outlogin_loc = (min_loc[1]['type'],min_loc[1]['value'])
        self.confirm_loc = (min_loc[2]['type'],min_loc[2]['value'])
        self.mine_loc = (min_loc[3]['type'],min_loc[3]['value'])
        self.login_loc = (page_loc[0]['type'], page_loc[0]['value'])
        self.wxlogin_loc = (page_loc[4]['type'], page_loc[4]['value'])
        self.wxcov_loc = (page_loc[5]['type'], page_loc[5]['value'])
        self.login_loc = (page_loc[0]['type'], page_loc[0]['value'])
        self.qqlogin_loc = (page_loc[6]['type'], page_loc[6]['value'])
        self.qqcov_loc = (page_loc[7]['type'], page_loc[7]['value'])
        self.btregist_loc = (zhuce_loc[0]['type'], zhuce_loc[0]['value'])
        self.alphone_loc = (zhuce_loc[1]['type'], zhuce_loc[1]['value'])
        self.arBtn_loc = (zhuce_loc[2]['type'], zhuce_loc[2]['value'])
        self.code_loc = (zhuce_loc[6]['type'], zhuce_loc[6]['value'])
        self.alkey_loc = (zhuce_loc[8]['type'], zhuce_loc[8]['value'])
        self.arregister_loc = (zhuce_loc[9]['type'], zhuce_loc[9]['value'])
        self.tvmale_loc = (zhuce_loc[11]['type'], zhuce_loc[11]['value'])
        self.nextstep_loc = (zhuce_loc[12]['type'], zhuce_loc[12]['value'])
        self.tvconfirm_loc = (zhuce_loc[13]['type'], zhuce_loc[13]['value'])
        self.tvreset_loc = (zhuce_loc[14]['type'], zhuce_loc[14]['value'])
        self.arnname_loc = (zhuce_loc[15]['type'], zhuce_loc[15]['value'])
        self.arnnextstep_loc = (zhuce_loc[16]['type'], zhuce_loc[16]['value'])
        self.tvfinish_loc = (zhuce_loc[17]['type'], zhuce_loc[17]['value'])
        self.dhbdclose__loc = (zhuce_loc[18]['type'], zhuce_loc[18]['value'])
        self.mine_loc = (min_loc[3]['type'],min_loc[3]['value'])
        self.userinfo_loc = (min_loc[4]['type'],min_loc[4]['value'])
        self.apiname_loc = (min_loc[5]['type'],min_loc[5]['value'])
        self.srfname_loc = (min_loc[6]['type'],min_loc[6]['value'])
        self.srfconfirm_loc = (min_loc[7]['type'],min_loc[7]['value'])

    def login(self, mobile, password):
        try:
            swipe_left(self.dr, 800, 5)
        except:
            pass
        self.click(self.login_loc)
        if mobile != '':
            self.clear_key(self.userphone_loc)
            self.send_keys(self.userphone_loc, mobile)
            self.send_keys(self.password_loc, password)
            self.click(self.userlogin_loc)
            self.always_allow()
            self.tan_chuan()
        else:
            self.send_keys(self.userphone_loc, mobile)
            self.send_keys(self.password_loc, password)
            self.click(self.userlogin_loc)
            self.always_allow()
            self.tan_chuan()

    def out_login(self):
        if self.find_element(self.mine_loc):
            self.click(self.mine_loc)
            swipe_up(self.dr, 500, 3)
            self.click(self.shezhi_loc)
            self.click(self.outlogin_loc)
            self.click(self.confirm_loc)

    def wx_login(self):
        try:
            swipe_left(self.dr, 800, 5)
        except:
            pass
        self.click(self.login_loc)
        self.click(self.wxlogin_loc)
        try:
            self.click(self.wxcov_loc)
        except:
            pass
        self.always_allow()

    def qq_login(self):
        try:
            swipe_left(self.dr, 800, 4)
        except:
            pass
        self.click(self.login_loc)
        self.click(self.qqlogin_loc)
        self.always_allow()
        try:
            self.click(self.qqcov_loc)
        except:
            pass
        self.always_allow()

    def chek_phone(self, mobile, password, code='000000'):
        self.send_keys(self.alphone_loc, mobile)
        self.click(self.arBtn_loc)
        self.send_keys(self.code_loc, code)
        self.send_keys(self.alkey_loc, password)
        self.click(self.arregister_loc)
        self.click(self.tvmale_loc)
        self.click(self.nextstep_loc)
        self.click(self.tvconfirm_loc)
        self.click(self.arnnextstep_loc)
        self.click(self.tvfinish_loc)
        self.click(self.dhbdclose__loc)

    def chek_regphone(self, mobile, code='000000'):
        self.send_keys(self.alphone_loc, mobile)
        self.click(self.arBtn_loc)
        self.send_keys(self.code_loc, code)
        self.click(self.arregister_loc)

    def zhu_ce(self, mobile, password='123456', code='000000'):
        try:
            swipe_left(self.dr, 800, 5)
        except:
            pass
        self.click(self.btregist_loc)
        self.send_keys(self.alphone_loc, mobile)
        self.click(self.arBtn_loc)
        self.send_keys(self.code_loc, code)
        self.send_keys(self.alkey_loc, password)
        self.click(self.arregister_loc)
        self.click(self.tvmale_loc)
        self.click(self.nextstep_loc)
        self.click(self.tvconfirm_loc)
        self.click(self.arnnextstep_loc)
        self.click(self.tvfinish_loc)
        self.click(self.dhbdclose__loc)

    def update_name(self, username):
        self.click(self.mine_loc)
        self.click(self.userinfo_loc)
        self.click(self.apiname_loc)
        self.send_keys(self.srfname_loc, username)
        self.click(self.srfconfirm_loc)

    def test_data(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        data_path = os.path.join(base_path, 'data', 'testdata.yaml')
        with open(data_path, 'rb') as fp:
            data = yaml.load(fp)
        # print(data)
        return data