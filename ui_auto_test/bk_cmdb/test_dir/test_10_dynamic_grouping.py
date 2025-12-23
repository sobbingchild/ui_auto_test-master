from time import sleep
from bk_cmdb.page import business
import seldom

from bk_cmdb.test_dir import test_01_login
from bk_cmdb import settings


class Dynamic_Grouping(seldom.TestCase):
    def test_01_new_dynamic_grouping(self):
        """新建动态分组（蓝鲸业务下）"""
        # 进入首页点击业务
        test_01_login.Login.test_login(self)
        sleep(2)
        test_01_login.Login.click_business(self)
        self.click(xpath=business.businessselector)
        # 等待后输入业务名并点击
        sleep(1)
        self.type(css=business.select_search_input, text=settings.BLUE_BUSINESS)
        self.click(xpath=business.option_name_blue_business)
        # 默认进入蓝鲸业务，展开Pass平台，点击apigw
        self.click(xpath=business.pass_platform)
        self.click(xpath=business.apigw)
        # 获取IP值
        global BluekingHostIp
        BluekingHostIp = self.get_text(xpath=business.get_host)
        print(BluekingHostIp)
        # 点击动态分组
        # self.is_visible(5,xpath=business.menu_name_dynamic_grouping)
        sleep(2)
        self.click(xpath=business.menu_name_dynamic_grouping)
        # 点击新建
        self.click(xpath=business.new)
        # 输入动态分组名称
        self.type(xpath=business.grouping_name,text=business.test)
        # 继续添加
        self.click(xpath=business.continue_add)
        # 点击SLA级别
        self.click(xpath=business.check_sla_level)
        # 确定添加条件，让鼠标失焦选中
        self.click(xpath=business.continue_add)
        # 选择SLA级别
        self.click(xpath=business.select_sla_level)
        # 选择SLA级别L1
        self.click(xpath=business.select_level_L1)
        #提交
        self.click(xpath=business.return_list_host)
        # 点击预览
        # self.is_visible(5,xpath=business.preview)
        sleep(2)
        self.click(xpath=business.preview)
        # 断言
        self.assertText(BluekingHostIp)

    def test_02_delete_dynamic_grouping(self):
        """删除动态分组（蓝鲸业务下）"""
        # 关闭窗口
        self.click(xpath=business.close_dynamic_grouping_window)
        # 点击删除
        # self.is_visible(5,xpath=business.delete)
        sleep(2)
        self.click(xpath=business.delete)
        # 确定删除
        self.click(xpath=business.sure_confirm)
        # 断言
        self.assertText(business.assert_delete)



