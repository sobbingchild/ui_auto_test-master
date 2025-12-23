 # -*- coding: utf-8 -*-
# @Time : 2021/8/16 17:22
# @File : test_03_file_transfer.py
# @Project : bk_job


from bk_job.page import file_transfer as page
from bk_job.test_dir.test_01_login import LoginBase
from pre_data.job_api_demo import JobApi
from bk_job.bk_exception import ApiError
import time

api = JobApi()


# 依赖IP
class FileTransfer(LoginBase):
    def test_01_server_file(self):
        '''分发服务器文件'''
        # 验证登录
        self._test_login()
        # 进入文件分发页面
        self.click(xpath=page.file_transfer)
        linux_ip_list = api.get_hosts_ip()
        if linux_ip_list and len(linux_ip_list)>=2:
            page.centos_1,page.centos_2 = linux_ip_list[0],linux_ip_list[1]
            print(page.centos_1)
            print(page.centos_2)
        else:
            ApiError('获取IP数量不符合预期，分发文件失败')
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
        self.type(xpath=page.host_search, text=page.centos_1)
        time.sleep(1)
        self.click(xpath=page.select_first_agent)
        print("文件服务器IP为:  " + self.get_text(xpath=page.first_agent_ip))
        self.click(xpath=page.confirm_agent)

        self.wait(3)
        # 保存表单
        self.click(xpath=page.save_button)
        # 输入目标路径
        self.type(xpath=page.dst_path, text=page.DST_PATH)
        self.sleep(1)

        # 滚动
        self.drag_and_drop_by_offset(xpath=page.scroll_bar, x=0, y=200)
        self.sleep(1)
        # 选择服务器
        self.click(xpath=page.execute_target)
        self.type(xpath=page.host_search, text=page.centos_2)
        time.sleep(1)
        self.click(xpath=page.select_first_agent)
        print("目标服务器IP为:  " + self.get_text(xpath=page.first_agent_ip))
        self.click(xpath=page.confirm_agent)

        self.click(xpath=page.button_excute_script)
        time.sleep(10)
        if self.get_text(xpath=page.status_excute) == page.excute_suss:
            print(page.excute_suss)
        elif self.get_text(xpath=page.status_excute) == page.excute_fail:
            print(page.excute_fail)
        else:
            print(page.excute_exception)
