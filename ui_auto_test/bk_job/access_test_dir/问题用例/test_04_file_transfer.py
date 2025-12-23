# -*- coding: utf-8 -*-
# @Time : 2021/8/16 17:22
# @File : test_03_file_transfer.py
# @Project : bk_job


import seldom
from bk_job.page import file_transfer as page
from bk_job.test_dir.test_01_login import LoginBase
import time


class FileTransfer(LoginBase):
    def test_01_server_file(self):
        # 登录态验证
        self._test_login()


        # 进入文件分发页面
        self.click(xpath=page.file_transfer)
        self.wait(3)
        # 断言是否进入页面成功
        self.assertText('分发文件')
        # 点击添加服务器文件
        self.click(xpath=page.server_file_button)
        self.wait(3)
        # 输入文件路径
        self.sleep(1)
        self.type(xpath=page.file_path, text=page.FILE_PATH)
        # 添加服务器
        self.click(xpath=page.add_host)
        self.sleep(1)

        # self.type(xpath=product_page.host_search,text=product_page.host_search_input)
        time.sleep(3)
        self.click(xpath=page.select_host)
        # print("文件服务器IP为:  " + self.get_text(xpath=page.select_host_ip))
        self.click(xpath=page.confirm_agent)

        self.wait(3)
        self.click(xpath=page.save_button)
        # 输入目标路径
        self.type(xpath=page.dst_path, text=page.DST_PATH)
        self.sleep(1)

        #滚动
        try:
            self.drag_and_drop_by_offset(xpath=page.scroll_bar,x=0, y=400)
        except Exception as A:
            print("当前页面无需滚动")
        #选择服务器
        self.click(xpath=page.execute_target)
        # self.type(xpath=product_page.host_search,text=product_page.host_search_input)
        time.sleep(3)
        self.click(xpath=page.select_first_agent)
        # print("目标服务器IP为:  " + self.get_text(xpath=page.first_agent_ip))
        self.click(xpath=page.confirm_agent)

        self.click(xpath=page.button_excute_script)
        time.sleep(10)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)

