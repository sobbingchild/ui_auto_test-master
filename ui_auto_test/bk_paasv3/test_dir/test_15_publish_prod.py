import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api

class Publish_Prod(seldom.TestCase):
    def test_01_get_access_address(self):
        """获取bk-esb中的prod的访问地址填入新建网关中的访问地址"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击云API
        self.click(xpath=cloud_api.cloud_api)
        # 跳转到界面第二个窗口并获取url跳转
        self.switch_to_window(1)
        global url
        url = self.get_url
        self.open(url)
        # 搜索框搜索网关
        self.type(xpath=cloud_api.search_gateway, text='bk-esb')
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_gateway).enter()
        # 点击网关bk-esb
        self.click(xpath=cloud_api.click_gateway_esb)
        # 点击环境管理
        self.click(xpath=cloud_api.environmental_management)
        # 编辑prod
        self.click(xpath=cloud_api.edit_prod)
        # 获取代理配置中的Hosts信息
        MyWebDriver.Keys(xpath=cloud_api.hosts).select_all()
        MyWebDriver.Keys(xpath=cloud_api.hosts).cut()
        # 点击我的网关
        self.click(xpath=cloud_api.my_gateway)
        # 搜索框搜索新建的网关
        self.type(xpath=cloud_api.search_gateway, text='test' + str(
            datetime.datetime.now().day))
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_gateway).enter()
        # 点击网关
        self.click(xpath=cloud_api.click_gateway)
        # 点击test16中的环境管理
        self.click(xpath=cloud_api.environmental_management)
        self.click(xpath=cloud_api.edit_prod)
        # + Hosts地址,- Hosts地址
        self.click(xpath=cloud_api.add_hosts)
        self.click(xpath=cloud_api.reduce_hosts)
        # 添加Hosts地址
        MyWebDriver.Keys(xpath=cloud_api.hosts).paste()
        # 提交编辑的Hosts信息
        self.click(xpath=cloud_api.commit_host)
        # 断言
        self.assertText(cloud_api.assert_update)
    def test_02_publish_prod(self):
        """prod发布"""
        # 鼠标悬浮
        self.move_to_element(xpath=cloud_api.mouse_hover)
        # 点击发布
        self.click(xpath=cloud_api.publish_prod)
        # 点击发布版本
        self.click(xpath=cloud_api.click_release_version)
        # 选择版本
        self.click(xpath=cloud_api.select_version)
        # 填写发布日志
        self.type(xpath=cloud_api.fill_in_the_publication_log,text='测试')
        # 发布
        self.click(xpath=cloud_api.release)
        # 确定
        self.click(xpath=cloud_api.sure_release)
        # 断言
        self.assertText(cloud_api.assert_under_release)


