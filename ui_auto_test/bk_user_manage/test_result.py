# -*- coding: utf-8 -*-
# @Time : 2020/10/23 16:19
# @File : test_result.py
# @Project : DevCenter_Uitest_G252
from bs4 import BeautifulSoup
import sys
import re
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bk_user_manage.base_operate import BaseOperate
from bk_user_manage import settings

base = BaseOperate()
with open('test_url.txt', 'w', encoding='utf-8') as txt:
    base.read_test_url()
    txt.write('测试环境为：' + settings.USER_URL + "\r\n")


def create_test_result(test_result_html, result):
    with open('test_result.txt', 'w', encoding='utf-8') as txt:
        txt.write(test_result_html + " " + result)


bs = BeautifulSoup(open('./reports/UserManage_ui_auto_test.html', encoding='utf-8'), 'lxml')

# print(bs.select('.text-right')[2].get_text())
test_result_text = bs.select('.text-right')[2].get_text()
# print(test_result_text)
# print(re.search('\w+', test_result_text).group())
if re.search('\w+', test_result_text).group() == 'Passed':
    # test_result = test_result_text.split()
    if 'Errors' in test_result_text:
        test_result = '有部分case fail/error失败'
        print(test_result)
        create_test_result(test_result_text, test_result)
        sys.exit(1)
    if 'Failed' in test_result_text:
        test_result = '有部分case fail/error失败'
        print(test_result)
        create_test_result(test_result_text, test_result)
        sys.exit(1)
    else:
        test_result = '测试case 全部success'
        print(test_result)
        create_test_result(test_result_text, test_result)
        sys.exit(0)
if re.search('\w+', test_result_text).group() == 'Failed' or re.search('\w+',
                                                                       test_result_text).group() == 'Errors':
    test_result = 'case 全error/fail 失败'
    print(test_result)
    create_test_result(test_result_text, test_result)
    sys.exit(1)
