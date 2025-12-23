# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_01_aply_perm.py
   Description : 
   Author :       v_adanchen
   date：          2022/4/8
-------------------------------------------------
"""
import bk_iam.page.ord_member as page
import time
from pre_data.user_api import UserApi
import bk_iam.settings as settings
import bk_iam.page.permission_group as pg
from bk_iam.access_test_dir import test_01_permission_group
from public_method import bk_exception
from bk_iam.base_operate import BaseOperate
import os
from public_method.login import LoginBase

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
base = BaseOperate()
base.path = PATH('../../../config.ini')


# @seldom.skip_if(base.read_data(key='check_flow') != 'True', '切换审批流程失败,用例跳过')
class ApplyPerm(LoginBase):
    def test_01_apply_perm(self):
        """创建普通用户申请-标准运维权限"""
        if not base.read_data(key='check_flow'):
            raise bk_exception.BluekingException('切换审批流程失败,用例跳过')
        userApi = UserApi()
        # 提前创建用户
        username = userApi.add_user()
        self.wait(1)
        print("username", username)
        # 重置密码
        pwd = userApi.user_passw()
        print("pwd", pwd)
        settings.NEW_USER = username
        settings.NEW_PWD = pwd
        # 调试代码 login页面
        # self._test_login(target_url=settings.IAM_URL, index_title=settings.INDEX_TITLE)
        self._test_login(target_url=settings.IAM_URL, index_title=settings.INDEX_TITLE, username=settings.NEW_USER,
                         pwd=settings.NEW_PWD)

        """申请权限"""
        # 进入权限申请页面
        self.sleep(2)
        self.click(xpath=page.perm_ply)
        # 进入申请自定义权限
        self.click(xpath=page.custom_perm)
        self.sleep(1)
        # 选择系统 - 标准运维
        self.click(xpath=page.select_system)
        self.click(xpath=page.select_sops)
        # 勾选访问标准运维-创建项目权限
        self.click(xpath=page.create_project)
        # 输入理由
        self.type(xpath=page.resean_type, text=page.resean_text)
        time.sleep(1)
        self.click(xpath=page.commit_ply)

    def test_02_login_out_iam(self):
        """退出iam"""
        if not base.read_data(key='check_flow'):
            raise bk_exception.BluekingException('切换审批流程失败,用例跳过')
        # 点击我是审批跳转到itsm
        self.sleep(1)
        self.click(xpath=page.nav_appro)
        # self.Keys.tab()
        # new_windows = self.window_handles[1]
        # print("新窗口----", new_windows)
        # self.switch_to_window(new_windows)
        self.switch_to_window(1)
        # 切换产品页面检查是否弹出通知中心
        self.check_notice()
        self.click(xpath=page.itsm_name)
        self.click(xpath=page.loginout_itsm)
        self.wait(3)

    def test_03_login_itsm(self):
        """登录itsm"""
        if not base.read_data(key='check_flow'):
            raise bk_exception.BluekingException('切换审批流程失败,用例跳过')
        self.login(settings.USER_NAME, settings.PASSWORD)

    def test_04_deal_approval(self):
        """处理权限审批"""
        if not base.read_data(key='check_flow'):
            raise bk_exception.BluekingException('切换审批流程失败,用例跳过')
        self.click(xpath=page.itsm_appro_pass)
        self.wait(1)
        self.click(xpath=page.itsm_appro_confrim, index=1)
        time.sleep(5)
        # new_windows = self.window_handles[0]
        # print("新窗口----", new_windows)
        # self.switch_to_window(new_windows)
        self.switch_to_window(0)

    def test_05_assert_perm(self):
        """检查是否获得权限"""
        """
        1.先切换到权限中心的窗口
        2.点击导航栏我的权限
        3.右上角切换账号，登录申请权限的这个用户
        4.点击 我的权限-自定义申请权限
        5.检查是否有标准运维的权限
        :return:
        """
        # new_windows = self.window_handles[0]
        # print("新窗口----", new_windows)
        # self.switch_to_window(new_windows)
        self.switch_to_window(0)
        self.click(xpath=page.nav_myperm)
        time.sleep(3)
        self.click(xpath=page.iam_name)
        time.sleep(1)
        self.click(xpath=page.iam_login_out)
        time.sleep(3)
        # self.login(settings.NEW_USER, settings.NEW_PWD)
        self._test_login(target_url=settings.IAM_URL, index_title=settings.INDEX_TITLE, username=settings.NEW_USER,
                         pwd=settings.NEW_PWD)
        self.refresh()
        self.sleep(2)
        self.click(xpath=page.nav_myperm)
        self.sleep(2)
        self.click(xpath=page.custom_review)
        time.sleep(2)
        self.click(xpath=page.Sops_permission)
        self.assertText(page.Sops)

    def test_06_change_approval_flow(self):
        """检查是否需要修改审批流程"""
        original_flow = base.read_data(key='original_flow')
        if test_01_permission_group.flow_name != original_flow:
            self.login(username=settings.USER_NAME, pwd=settings.PASSWORD)
            self.sleep(0.5)
            self.click(xpath=pg.permission_group_tab, index=1)
            self.sleep(0.5)
            # 进入审批流程
            self.click(xpath=pg.approval_flow_tab)
            self.click(xpath=pg.sys_permission_select)
            self.click(xpath=pg.sys_li_select)
            self.sleep(2)
            self.refresh()
            self.assertText(page.Sops)
            # if original_flow in '分级管理员审批':
            if original_flow in '告警分派':
                try:
                    # print('分级管理员审批')
                    print('告警分派')
                    self.slow_click(xpath=pg.approval_flow)
                    self.sleep(0.5)
                    self.type(xpath='//input[@placeholder="请输入关键字搜索"]', text=original_flow)
                    text = self.get_text(xpath=pg.warnings_flow)
                    print('text' + text)
                    print('original_flow' + original_flow)
                    self.click(xpath=pg.warnings_flow)
                    self.sleep(0.2)
                    self.assertText('操作成功')
                except Exception as e:
                    raise bk_exception.BluekingException(
                        '切换审批流程失败 error messages : {}'.format(e)
                    )
            elif original_flow in '用户组审批流程':
                try:
                    print('用户组审批流程')
                    self.slow_click(xpath=pg.approval_flow)
                    self.sleep(0.5)
                    self.type(xpath='//input[@placeholder="请输入关键字搜索"]', text=original_flow)
                    text = self.get_text(xpath=pg.original_flow)
                    print('text' + text)
                    print('original_flow' + original_flow)
                    self.click(xpath=pg.original_flow)
                    self.sleep(0.2)
                    self.assertText('操作成功')
                except Exception as e:
                    raise bk_exception.BluekingException(
                        '切换审批流程失败 error messages : {}'.format(e)
                    )
        else:
            print('无需切换流程')

    def login(self, username, pwd):
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
            self.refresh()
            self.check_notice()

        except BaseException as e:
            print("登录失败", e)
