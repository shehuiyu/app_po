import sys
import os
sys.path.append(os.getcwd())
import pytest
from tool import read_yml
from page.page_login import PageLogin





class TestLogin():
    # 初始化
    def setup_class(self):
        self.login = PageLogin()
        self.login.click_close_alert()
        self.login.click_me()
        self.login.click_username_exists()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 测试方法
    @pytest.mark.parametrize('username,password', read_yml.read_yml())
    def test_login(self, username, password):
        self.login.page_login(username, password)
