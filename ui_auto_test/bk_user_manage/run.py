import seldom
import click
import logging
import sys
import os
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bk_user_manage.base_operate import BaseOperate

base = BaseOperate()
logging.basicConfig(level=logging.INFO, format='%(asctime)s''- %(levelname)s: %(message)s')


@click.command()
@click.option('--report', help='report save directory')
@click.option('--html_title', help='report title')
@click.option('--test_model', default='True', help='choice test model default=True run assess_test')
def main(report, html_title,test_model):
    """
    example:python run.py  --report=Index.html --html_title=test_title --test_model=True
    """
    # 命令行不输入url时则默认使用207环境进行测试
    url=base.read_test_url()
    model = test_model.capitalize()
    if url == False:
        sys.exit(1)
    password=base.read_admin_password()
    if password == False:
        sys.exit(1)
    test_path = base.choice_test_model(model=model)
    if test_path == False:
        sys.exit(1)
    seldom.main(
        path=test_path,
        #path='./test_dir/test_08_delete_project_task.py',
        report=report,
        title=html_title,
        browser="chrome",
        timeout=10,
        debug=False
                )

if __name__ == '__main__':
    # 调试代码时 debug=True,自动化上线时为false。 同时修改path路径指向test_dir
    main()
    # seldom.main(
    #     path='./test_dir/',
    #     debug=False)