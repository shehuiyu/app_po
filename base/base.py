from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化driver对象
    def __init__(self):
        caps = {'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': '192.168.56.101:5555',
                'appPackage': 'com.yunmall.lc',
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity'}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    # 查找元素方法
    def base_find(self, loc, timeout=10, poll=0.5, ):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find(loc)
        # 清空输入框
        el.clear()
        # 输入值
        el.send_keys(value)
