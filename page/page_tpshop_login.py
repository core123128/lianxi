from base.base import Base
import page


class PageTPshopLogin(Base):
    # 点击登录
    def page_click_login01(self):
        self.base_click(page.tp_login_btn01)

   # 输入用户名
    def page_input_username(self,username):
        self.base_input_value(page.tp_login_username,username)

   # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input_value(page.tp_login_pwd,pwd)


   # 输入验证码
    def page_input_code(self,code):
        self.base_input_value(page.tp_login_code,code)

   # 点击登录
    def page_click_login02(self):
        self.base_click(page.tp_login_btn02)
   # 获取弹窗的文本信息
    def page_get_text(self):
        return self.base_get_text(page.tp_login_text)


   # 组合业务
    def page_login(self,username,pwd,code):
        self.page_click_login01()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_click_login02()
        return self.page_get_text()