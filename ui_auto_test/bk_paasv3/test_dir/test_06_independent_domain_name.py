import seldom

from bk_paasv3.test_dir import test_01_login
from bk_paasv3.page import application_development
from public_method.keyboard_operation import MyWebDriver

class Independent_Domain_Name(seldom.TestCase):
    def test_01_add_domain_name(self):
        """添加域名、编辑域名、删除域名（独立域名）"""
        # 进入首页
        test_01_login.Login.test_login(self)
        # 点击应用开发
        self.click(xpath=application_development.application_development)
        # 搜索框搜索应用
        self.type(xpath=application_development.search_application,text="标准运维")
        # 模拟enter键
        MyWebDriver.Keys(xpath=application_development.search_application).enter()
        # 应用
        self.click(xpath=application_development.click_application)
        # 应用引擎
        self.click(xpath=application_development.application_engine)
        # 访问入口
        self.click(xpath=application_development.access_entry)
        # 点击独立域名
        self.click(xpath=application_development.independent_domain_name)
        # 添加域名
        self.click(xpath=application_development.add_domain_name)
        # 点击环境选择环境
        self.click(xpath=application_development.environment)
        # 选择环境为预发布环境
        self.click(xpath=application_development.select_environment)
        # 输入域名
        self.type(xpath=application_development.input_domain_name,text='www.baidu.com')
        # 点击绑定模块选择模块
        self.click(xpath=application_development.binding_modules)
        # 选择default模块
        self.click(xpath=application_development.select_modules)
        # 确定
        self.click(xpath=application_development.sure_domain_name)
        # 断言添加域名
        self.assertText(application_development.assert_add_success)
        # 编辑
        self.click(xpath=application_development.edit_domain_name)
        # 更改路径
        self.type(xpath=application_development.chang_path,text='data')
        # 确定
        self.click(xpath=application_development.sure_domain_name)
        # 断言编辑域名
        self.assertText(application_development.assert_update_success)
        # 删除
        self.click(xpath=application_development.delete_domain_name)
        # 确定删除
        self.click(xpath=application_development.sure_delete_domain_name)
        # 断言删除域名
        self.assertText(application_development.assert_delete_domain_name)




