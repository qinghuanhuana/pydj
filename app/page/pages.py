from app.page import tools
pages = tools.parseyaml()

def get_locator(clazz_name, method_name):
     locators = pages[clazz_name]['locators']
     for locator in locators:
          if locator['name'] == method_name:
               return locator



class LonginPage:
      引导页登陆0 = get_locator("LonginPage", "引导页登陆0")
      用户手机号1 = get_locator("LonginPage", "用户手机号1")
      用户密码2 = get_locator("LonginPage", "用户密码2")
      登陆页登陆3 = get_locator("LonginPage", "登陆页登陆3")
      微信登陆4 = get_locator("LonginPage", "微信登陆4")
      确认登录5 = get_locator("LonginPage", "确认登录5")
      qq登录6 = get_locator("LonginPage", "qq登录6")
      登录7 = get_locator("LonginPage", "登录7")
      登录7 = get_locator("LonginPage", "登录7")
      登录7 = get_locator("LonginPage", "登录7")
      
class MinePage:
      设置0 = get_locator("MinePage", "设置0")
      退出当前登陆1 = get_locator("MinePage", "退出当前登陆1")
      确定2 = get_locator("MinePage", "确定2")
      我的主页3 = get_locator("MinePage", "我的主页3")
      用户信息4 = get_locator("MinePage", "用户信息4")
      用户名称5 = get_locator("MinePage", "用户名称5")
      用户名输出框6 = get_locator("MinePage", "用户名输出框6")
      用户名更改确认7 = get_locator("MinePage", "用户名更改确认7")
      用户乐心id8 = get_locator("MinePage", "用户乐心id8")
      
class ShouyePage:
      首页0 = get_locator("ShouyePage", "首页0")
      运动1 = get_locator("ShouyePage", "运动1")
      发现2 = get_locator("ShouyePage", "发现2")
      我的3 = get_locator("ShouyePage", "我的3")
      首页挑战4 = get_locator("ShouyePage", "首页挑战4")
      首页分享5 = get_locator("ShouyePage", "首页分享5")
      首页号6 = get_locator("ShouyePage", "首页"+"号6")
      首页步数目标7 = get_locator("ShouyePage", "首页步数目标7")
      首页有氧运动时长8 = get_locator("ShouyePage", "首页有氧运动时长8")
      有氧时长标题9 = get_locator("ShouyePage", "有氧时长标题9")
      有氧时长统计10 = get_locator("ShouyePage", "有氧时长统计10")
      更多11 = get_locator("ShouyePage", "更多11")
      设置周目标12 = get_locator("ShouyePage", "设置周目标12")
      选择目标13 = get_locator("ShouyePage", "选择目标13")
      周目标确定14 = get_locator("ShouyePage", "周目标确定14")
      保存周目标15 = get_locator("ShouyePage", "保存周目标15")
      所需目标16 = get_locator("ShouyePage", "所需目标16")
      目标距离17 = get_locator("ShouyePage", "目标距离17")
      首页有氧能力提升计划18 = get_locator("ShouyePage", "首页有氧能力提升计划18")
      有氧能力提升计划跳过19 = get_locator("ShouyePage", "有氧能力提升计划跳过19")
      有氧能力提升计划标题20 = get_locator("ShouyePage", "有氧能力提升计划标题20")
      有氧能力提升计划更多21 = get_locator("ShouyePage", "有氧能力提升计划更多21")
      
class ZhucePage:
      注册按钮0 = get_locator("ZhucePage", "注册按钮0")
      手机号输入1 = get_locator("ZhucePage", "手机号输入1")
      下一步2 = get_locator("ZhucePage", "下一步2")
      微信登陆3 = get_locator("ZhucePage", "微信登陆3")
      图像验证码输入4 = get_locator("ZhucePage", "图像验证码输入4")
      图片验证码刷新5 = get_locator("ZhucePage", "图片验证码刷新5")
      短信验证码输入6 = get_locator("ZhucePage", "短信验证码输入6")
      获取短信验证码7 = get_locator("ZhucePage", "获取短信验证码7")
      密码输入8 = get_locator("ZhucePage", "密码输入8")
      点击注册9 = get_locator("ZhucePage", "点击注册9")
      qq登陆10 = get_locator("ZhucePage", "qq登陆10")
      选择男11 = get_locator("ZhucePage", "选择男11")
      个人资料下一步12 = get_locator("ZhucePage", "个人资料下一步12")
      确认无误13 = get_locator("ZhucePage", "确认无误13")
      重新修改14 = get_locator("ZhucePage", "重新修改14")
      用户昵称输入15 = get_locator("ZhucePage", "用户昵称输入15")
      个人资料下一步16 = get_locator("ZhucePage", "个人资料下一步16")
      目标设置完成17 = get_locator("ZhucePage", "目标设置完成17")
      关闭18 = get_locator("ZhucePage", "关闭18")
      qq登陆10 = get_locator("ZhucePage", "qq登陆10")

if __name__ == '__main__':
     loc = LonginPage.引导页登陆0
     print(loc)