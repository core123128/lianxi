import pytest

from page.page_tpshop_login import PageTPshopLogin
from tools.untils import GetDriver

def get_data():
    return [(18888888888,12345,8888,'密码错误'),(10000000000,123456,8888,'账号不存在')]


class TestTPLogin:
    def setup_class(self):
        # 初始化
        self.driver=GetDriver.get_driver()
        # 从公共工具类中获取driver对象
        self.tplogin=PageTPshopLogin()
        # 初始化page层中的PageTPshopLogin对象

    def teardown_class(self):
        # 结束
        # 关闭driver对象
        GetDriver.quit_driver()
    def setup(self):
        self.driver.get('http://localhost/index.php')

    @pytest.mark.parametrize('username,pwd,code,info',get_data())
    def test_tpshop_login(self,username,pwd,code,info):
        #     测试方法
        text=self.tplogin.page_login(username,pwd,code)
        assert info in text

        # assert '密码错误' in 'self.tplogin'
# if __name__ == '__main__':
#     pytest.main('-s test_tp_login.py')

