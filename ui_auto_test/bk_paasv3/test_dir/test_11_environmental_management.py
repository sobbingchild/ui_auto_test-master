import seldom

from bk_paasv3.test_dir import test_01_login
import datetime
from public_method.keyboard_operation import MyWebDriver
from bk_paasv3.page import cloud_api
from time import sleep

class Environmental_Management(seldom.TestCase):
    def test_01_deployment_restrictions(self):
        """新建/编辑环境"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击云API
        self.click(xpath=cloud_api.cloud_api)
        # 跳转到界面第二个窗口并获取url跳转
        self.switch_to_window(1)
        global url
        url = self.get_url
        self.open(url)
        # 搜索框搜索新建的网关
        self.type(xpath=cloud_api.search_gateway, text='test' + str(
            datetime.datetime.now().day))
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_gateway).enter()
        # 点击网关
        self.click(xpath=cloud_api.click_gateway)
        # 点击环境管理,设置等待时间，防止界面不可点击
        self.click(xpath=cloud_api.environmental_management)
        sleep(3)
        # 新建环境
        self.click(xpath=cloud_api.new_environment)
        # 新建环境名称
        self.type(xpath=cloud_api.new_environment_name,text='test1230')
        # 输入Hosts
        self.type(xpath=cloud_api.enter_host,text='https://test.bking.com')
        # 提交
        self.click(xpath=cloud_api.commit_host)
        self.assertText(cloud_api.assert_successful_creation)
        # 点击编辑
        self.click(xpath=cloud_api.click_edit)
        # 点击新增(环境变量)
        self.click(xpath=cloud_api.new_environment_variable)
        # 输入变量名及值
        self.type(xpath=cloud_api.input_variable_name,text='id')
        self.type(xpath=cloud_api.input_variable_value,text='1')
        # 确定
        self.click(xpath=cloud_api.sure_environment_variable)
        # 提交
        self.click(xpath=cloud_api.commit_environment_variable)
        self.assertText(cloud_api.assert_update)
    def test_02_release_version(self):
        """生成版本、发布版本"""
        # 鼠标悬浮
        self.move_to_element(xpath=cloud_api.mouse_hover)
        # 点击发布
        self.click(xpath=cloud_api.publish)
        # 点击版本管理
        self.click(xpath=cloud_api.version_management)
        # 生成版本
        self.click(xpath=cloud_api.generated_version)
        # 填写版本号
        self.type(xpath=cloud_api.fill_in_version_number,text='1.0.0')
        # 填写标题
        self.type(xpath=cloud_api.fill_in_the_title,text='测试用')
        # 生成
        self.click(xpath=cloud_api.generate)
        # 断言
        self.assertText(cloud_api.assert_successful_version_generation)
        # 发布版本
        self.click(xpath=cloud_api.release_version)
        # 点击环境
        self.click(xpath=cloud_api.environment)
        # 选择环境test1230
        self.click(xpath=cloud_api.select_environment)
        # 填写发布日志
        self.type(xpath=cloud_api.fill_in_the_publication_log,text='测试')
        # 发布
        self.click(xpath=cloud_api.release)
        # 确定
        self.click(xpath=cloud_api.sure_release)
        # 断言
        self.assertText(cloud_api.assert_under_release)
    def test_03_search_environmental(self):
        """搜索环境名称"""
        # 点击×
        self.click(xpath=cloud_api.clear)
        # 点击基本设置
        self.click(xpath=cloud_api.basic_setup)
        # 点击环境管理,设置等待时间，防止界面不可点击
        self.click(xpath=cloud_api.environmental_management)
        sleep(3)
        # 搜索框搜索环境名称
        self.type(xpath=cloud_api.search_environmental_name,text='test1230')
        # 模拟enter键
        MyWebDriver.Keys(xpath=cloud_api.search_environmental_name).enter()
        # 断言
        self.assertText(cloud_api.assert_have_published)
    def test_04_Off_line_delete_environment(self):
        """删除环境"""
        # 鼠标悬浮
        self.move_to_element(xpath=cloud_api.mouse_hover)
        # 点击下线
        self.click(xpath=cloud_api.offline)
        # 点击确定
        self.click(xpath=cloud_api.sure_offline)
        # 断言
        self.assertText(cloud_api.assert_offline_success)
        # 鼠标悬浮
        self.move_to_element(xpath=cloud_api.mouse_hover)
        # 删除
        self.click(xpath=cloud_api.delete_environment)
        # 确定删除环境
        self.click(xpath=cloud_api.sure_delete_environment)
        # 断言
        self.assertText(cloud_api.assert_delete_successfully)

        




