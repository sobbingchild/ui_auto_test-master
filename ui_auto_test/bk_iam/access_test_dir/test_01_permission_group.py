import bk_iam.page.ord_member as page
import time
import bk_iam.settings as settings
import bk_iam.page.permission_group as pg
from public_method import bk_exception
from bk_iam.base_operate import BaseOperate
import os
from public_method.login import LoginBase

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
permission_group_name = '超级管理员'
permission_manage_space = '标准运维'
flow_name = '默认审批流程'
original_flow = ''
check_flow = False


class CheckPermissionGroup(LoginBase):
    def test_01_enter_permission_group(self):
        """进入权限中心--管理空间"""
        self.open(settings.IAM_URL)
        #self._test_login(target_url=settings.IAM_URL, index_title=settings.INDEX_TITLE)
        # self.login(username=settings.USER_NAME, pwd=settings.PASSWORD)
        self.sleep(3)
        self.click(xpath=pg.permission_group_tab, index=1)
        self.sleep(3)
        # 判断是否进入管理空间
        try:
            group = self.get_text(xpath=pg.form_title, index=1)
            print(group)
            assert group == '用户组'
        except Exception as e:
            raise bk_exception.BluekingException(
                '进入管理空间失败-断言失效 error_messages ：{}'.format(e)
            )
        print('进入管理空间')
        group_name = self.get_text(xpath=pg.permission_group)
        print(group_name)
        if group != permission_group_name:
            self.click(xpath=pg.permission_group)
            self.sleep(0.5)
            self.type(xpath=pg.permission_group_input, text=permission_group_name)
            self.click(xpath=pg.permission_group_name.format(permission_group_name))
        self.sleep(0.5)

    def test_02_enter_approval_flow(self):
        """管理空间--进入审批流程"""
        # 进入审批流程
        self.click(xpath=pg.approval_flow_tab)
        approval_flow = self.get_text(xpath=pg.form_title)
        if approval_flow != '审批流程':
            bk_exception.BluekingException(
                '进入审批流程页面失败-断言失效'
            )
        print('进入审批流程')
        manage_space = self.get_text(xpath=pg.product_space)
        if manage_space != permission_manage_space:
            self.click(xpath=pg.product_space)
            self.sleep(0.5)
            self.click(xpath=pg.product_space_name)
            self.assertText('项目查看')
            self.refresh()

    def test_03_check_approval_flow(self):
        """标准运维-项目查看-检查审批流程-并切换为默认审批流程"""
        try:
            flow = self.get_text(xpath=pg.approval_flow)
            print(flow)
            base = BaseOperate()
            base.path = PATH('../../../config.ini')
            print(base.path)
            base.write_data(key='original_flow', value=flow)

            # global original_flow
            # original_flow = flow
        except Exception as e:
            raise bk_exception.BluekingException(
                '获取审批流程失败 error messages : {}'.format(e)
            )
        if flow != flow_name:
            try:
                self.slow_click(xpath=pg.approval_flow)
                self.sleep(0.5)
                self.click(xpath=pg.default_flow)
                base.write_data(key='check_flow', value='True')
            except Exception as e:
                raise bk_exception.BluekingException(
                    '切换审批流程失败 error messages : {}'.format(e)
                )
        else:
            base.write_data(key='check_flow', value='True')
            self.sleep(1)
        # global check_flow
        # check_flow = True
        print('检查审批流程完成')
        # print(check_flow)
        # print(base.read_data(key='check_flow'))
        # print(type(base.read_data(key='check_flow')))
        # print(base.read_data(key='original_flow'))

    def login(self, username, pwd):
        self.set_window(1920, 1080)
        self.delete_all_cookies()
        self.refresh()
        self.sleep(1)
        try:
            # 输入账号
            self.type(xpath=page.account, text=username)
            # 输入密码
            self.type(xpath=page.password, text=pwd)
            self.click(xpath=page.login_btn)
            time.sleep(3)
        except BaseException as e:
            print("登录失败", e)
