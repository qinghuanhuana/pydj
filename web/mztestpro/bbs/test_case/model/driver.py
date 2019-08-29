from selenium import webdriver


def browser(br='chrome'):
    global driver
    if br == 'chrome':
        driver = webdriver.Chrome()
    elif br == 'ie':
        driver = webdriver.Ie()
    elif br == 'ff':
        driver = webdriver.Firefox()
    else:
        print('参数错误')
    return driver


if __name__ == '__main__':
    dr = browser('ff')
    dr.get('http://www.baidu.com')
    dr.quit()
