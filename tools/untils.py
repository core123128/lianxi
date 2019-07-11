from selenium import webdriver


class GetDriver(object):
    # 创建一个公共工具类，里面实现初始化driver对象的方法和关闭driver对象的方法
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.get('http://localhost/index.php')
            cls.driver.maximize_window()
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None