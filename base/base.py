from selenium.webdriver.support.wait import WebDriverWait

from tools.untils import GetDriver


class Base(object):
    # 创建基类，把page层面操作都放在基类中
    def __init__(self):
        self.driver=GetDriver.get_driver()
    def base_find(self,loc,time=30,poll=0.5):
        # 这里的loc参数传入是一个元素形式，元祖解包可以用*loc的方式
        # 每个元素都设置显示等待，因为调用显示等待方法返回的就是元素操作对象
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))
        # 一定要返回，因为这里调用这个方法获取元素
    def base_click(self,loc):
        # 这个是元素点击方法
        self.base_find(loc).click()
    def base_input_value(self,loc,value):
        # 这个是元素的send_keys方法
        self.base_find(loc).send_keys(value)
    def base_get_text(self,loc):
        # 获取文本信息
        return self.base_find(loc).text