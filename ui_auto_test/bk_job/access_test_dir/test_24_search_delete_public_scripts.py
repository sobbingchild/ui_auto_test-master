# -*- coding: utf-8 -*-
# @Time : 2021/10/24 15:18
# @File : test_23_search_delete_public_scripts.py
# @Project : bk_job
from bk_job.test_dir.test_01_login import LoginBase
from bk_job.page import public_script as page
from bk_job.page import delete_script_page as del_page
from bk_job.bk_exception import ApiError
from pre_data.job_api_demo import JobApi
from bk_job import settings

api = JobApi()


# 创建shell脚本
class SearchShellScript(LoginBase):
    def test_01_searchShell(self):
        '''搜索公共脚本'''
        # 登录态验证
        self._test_login()
        # 进入平台管理页面
        self.click(xpath=page.public_script_list)
        self.sleep(1)
        # 断言进入公共脚本页面
        self.assertText('公共脚本')
        self.type(xpath=page.public_search_textarea, text=page.PUBLIC_SHELL_SCRIPT_NAME)
        self.sleep(1)
        self.click(xpath=page.table_name)
        script_name = self.get_text(xpath=page.script_name)
        assert script_name == page.PUBLIC_SHELL_SCRIPT_NAME
        print('公共脚本名称搜索成功')

    def test_02_deleteShell(self):
        '''删除公共脚本'''
        self.click(xpath='//div[@data-test-id="page_publicScriptList"]')
        # 点击 删除shell脚本
        self.click(xpath=del_page.del_button())
        self.wait(3)
        # 断言提示框文本
        delete_alert_text = self.get_text(xpath=del_page.delete_alert_text)
        assert delete_alert_text == del_page.DELETE_ALERT_TEXT
        # 点击 确定 删除脚本
        self.click(xpath=del_page.delete_alert_button)
        self.assertText('删除成功')
        print('删除公共shell脚本成功')

    def test_03_delete_api_tmp(self):
        '''调用api删除对应创建的模板'''
        if not settings.COMMON_ID and settings.CRON_ID:
            raise ApiError('没有模板ID无法删除')
        try:
            del_result_1 = api.del_template(template_id=settings.COMMON_ID)
            print(del_result_1)
            self.sleep(2)
            del_result_2 = api.del_template(template_id=settings.CRON_ID)
            print(del_result_2)
            assert del_result_1 and del_result_2 == True
        except Exception as e:
            raise ApiError(e)
