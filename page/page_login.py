from base.base import Base
import page


class PageLogin(Base):
    # 关闭弹窗
    def click_close_alert(self):
        self.base_click((page.login_close_alert))

    # 点击我
    def click_me(self):
        self.base_click(page.login_me)

    # 点击已有账号去登陆
    def click_username_exists(self):
        self.base_click(page.login_username_exists)

    # 输入账号
    def input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def input_password(self, password):
        self.base_input(page.login_pwd, password)

    # 点击登录
    def click_login_btn(self):
        self.base_click(page.login_btn)

    # 业务组合
    def page_login(self, username, password):
        # self.click_close_alert()
        # self.click_me()
        # self.click_username_exists()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
#
# if __name__ == '__main__':
#     a = PageLogin()
#     a.page_login('itheima','123456')
