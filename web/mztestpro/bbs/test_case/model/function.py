from selenium import webdriver
import os, time


# 截图
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    base_dir = str(base_dir)
    file_path = base_dir + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.get("http://www.baidu.com")
    dr.set_window_size(700, 700)
    try:
        dr.find_element_by_id('kw').send_keys('测试')
        time.sleep(2)
        dr.find_element_by_id('su').click()
        time.sleep(2)
        dr.execute_script('window.scrollTo(500,450)')
    except Exception as e:
        print(e)
    # insert_img(dr, 'baidu.png')
    # dr.quit()