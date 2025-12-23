from bs4 import BeautifulSoup
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bk_monitor.base_operate import BaseOperate
from bk_monitor import settings

base = BaseOperate()
with open('test_url.txt', 'w', encoding='utf-8') as txt:
    base.read_test_url()
    txt.write('测试环境为：' + settings.MONITOR_URL + "\r\n")


def create_test_result(test_result_html, result):
    with open('test_result.txt', 'w', encoding='utf-8') as txt:
        txt.write(test_result_html + " " + result)

bs = BeautifulSoup(open('./reports/Monitor_ui_auto_test.html', encoding='utf-8'), 'lxml')

print(bs.select('.text-sm')[3].get_text().strip().split('\n'))

test_result_text = bs.select('.text-sm')[3].get_text().strip().split('\n')
result_dict = {}
for result in test_result_text:
    result_list = result.split(':')
    result_dict[result_list[0]] = result_list[1]
for i in result_dict:
    if i not in 'Passed' and int(result_dict[i]) > 0:
        test_result = '有部分case fail/error失败'
        create_test_result(str(test_result_text), test_result)
        sys.exit(1)
test_result = '测试case 全部success'
create_test_result(str(test_result_text), test_result)
