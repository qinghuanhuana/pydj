import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get('http://www.baidu.com')
t1 = dr.find_element_by_link_text('设置')
'''
单击 click()
双击 double_click()
右击 context_click()
单击不放 click_and_drop()
拖拽  drag_and_drop()
拖动至 drag_and_drop_by_offset()
按下键盘键 key_down()
松开键盘键 key_up()
鼠标移动 move_by_offset()
鼠标移动至 mover_to_element()
松开鼠标左键 release()
'''
action = ActionChains(dr)
# action.move_to_element(t1).perform()
# t2 = dr.find_element_by_link_text('搜索设置')
# action.click(t2).perform()
action.key_up(Keys.SHIFT).key_down(Keys.SHIFT).perform()

