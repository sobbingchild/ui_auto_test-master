# -*- coding: utf-8 -*-
# @Time : 2022/1/18 15:42
# @File : base_operate.py

from bk_iam import settings
import logging
import os
from bk_iam.base_info import BaseInfomation

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
logging.basicConfig(level=logging.INFO, format='%(asctime)s''- %(levelname)s: %(message)s')
Base_info = BaseInfomation()


class BaseOperate():
    def __init__(self):
        # self.path = PATH('config.ini')
        self.path = PATH('../../config.ini')

    # 读数据
    def read_data(self, key, sessiondata='testdata'):
        data = Base_info.read_config_one(sessiondata, key, self.path)
        return data

    def write_data(self, key, value,):
        data = Base_info.write_config(key,value,self.path)
        return data

    # 返回首页地址
    def read_test_url(self):
        ''' 获取配置文件中的URL'''
        url = self.read_data(key=settings.IAM_URL)
        if not url:
            logging.info('无法获取对应测试环境URL,测试结束')
            return False
        elif 'ee207' in url:
            settings.ENVIRONMENT = False
            settings.IAM_URL = url
            logging.info('测试地址获取成功')
            logging.info('当前测试地址为{}'.format(settings.IAM_URL))
            return url
        else:
            settings.ENVIRONMENT = True
            settings.IAM_URL = url
            settings.BIZ_NAME = '蓝鲸'
            logging.info('测试地址获取成功')
            logging.info('当前测试地址为{}'.format(settings.IAM_URL))
            return url

    def read_admin_password(self):
        ''' 判断admin密码'''
        password = self.read_data(key=settings.PASSWORD)
        if not password:
            logging.info('admin密码获取失败,测试结束')
            return False
        else:
            settings.PASSWORD = password
            logging.info('admin密码获取成功')
            return password

    def choice_test_model(self, model):
        if model == 'True':
            logging.info('运行准入用例')
            path = './access_test_dir/'
            return path
        elif model == 'False':
            logging.info('运行全量用例')
            path = './test_dir/'
            return path
        else:
            logging.info('test_model只允许输入True OR False,请输入正确的关键字')
            return False


if __name__ == '__main__':
    test = BaseOperate()
