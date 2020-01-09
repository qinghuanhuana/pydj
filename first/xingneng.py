import os, time, platform

def starttime_app(packagename, packgenameactivity):
    cmd = 'adb shell am start -W -n %s' %packagename + '/' + packgenameactivity
    print(os.popen(cmd).read())
    me = os.popen(cmd).read().split('\n')[-7].split(':')
    cmd2 = 'adb shell am force-stop %s' %packagename
    os.system(cmd2)
    return me

a = starttime_app('gz.lifesense.weidong.qa', 'gz.lifesense.weidong.ui.activity.login.intl.MobileLoginActivity'
)
print(a)