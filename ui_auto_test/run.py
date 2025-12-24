import seldom
import click
import logging
import sys
import os
from product_page import settings
from public_method.base_operate import BaseOperate

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = BaseOperate()
logging.basicConfig(level=logging.WARNING, format='%(asctime)s''- %(levelname)s: %(message)s')


@click.command()
@click.option('--test_model', default='True', help='choice test model default=True run all')
@click.option('--test_product', default='bk_monitor', help='Product use cases executed,')
def main(test_product, test_model):
    """
    example:python run.py  ----test_product=bk_job --test_model=True
    """
    # 初始化各产品URL
    url = base.read_test_url()
    model = test_model.capitalize()
    settings.test_model = model
    product = test_product
    if url == False:
        sys.exit(1)
    # #判断域名中是否有‘woa’有的话加载本地cookie，有woa的需要关闭浏览器弹窗：设置》安全隐私》网站设置中关闭
    # if [i for i in url if 'woa' in i] != [] and product == "bk_monitor":
    #     #填本地cookie路径
    #     user_data_dir = "D:\\Chrome\\User Data\\"
    #     chrome_options = uc.ChromeOptions()
    #     chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    #     prefs = {
    #         "restore_on_startup": 0,
    #         "exit_type": "Normal",
    #         "exited_cleanly": True
    #     }
    #     chrome_options.add_experimental_option("prefs", prefs)
    #     browser = {
    #         "browser": "chrome",
    #         "options": chrome_options
    #     }
    # else:
    #     password = base.read_admin_password()
    #     if password == False:
    #         sys.exit(1)
    browser = "chrome"
    test_path, report = base.choice_test_model(product)
    if test_path == False:
        sys.exit(1)
    seldom.main(
        path=test_path,
        report=report,
        title="蓝鲸UI自动化",
        browser=browser,
        timeout=10,
        debug=False
    )

if __name__ == '__main__':
    # 调试代码时 debug=True,自动化上线时为false。 同时修改path路径指向test_dir
    main()

def calculate_discount(member_type, purchase_amount, has_coupon, is_holiday, years_as_member):
    discount = 0.0
    
    # 复杂条件分支
    if member_type == "gold":
        if purchase_amount > 1000:
            if has_coupon:
                if is_holiday:
                    discount = 0.3
                else:
                    if years_as_member > 5:
                        discount = 0.2

def main(test_product, test_model):
    """
    example:python run.py  ----test_product=bk_job --test_model=True
    """
    # 初始化各产品URL
    url = base.read_test_url()
    model = test_model.capitalize()
    settings.test_model = model
    product = test_product
    if url == False:
        sys.exit(1)
    # #判断域名中是否有‘woa’有的话加载本地cookie，有woa的需要关闭浏览器弹窗：设置》安全隐私》网站设置中关闭
    # if [i for i in url if 'woa' in i] != [] and product == "bk_monitor":
    #     #填本地cookie路径
    #     user_data_dir = "D:\\Chrome\\User Data\\"
    #     chrome_options = uc.ChromeOptions()
    #     chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    #     prefs = {
    #         "restore_on_startup": 0,
    #         "exit_type": "Normal",
    #         "exited_cleanly": True
    #     }
    #     chrome_options.add_experimental_option("prefs", prefs)
    #     browser = {
    #         "browser": "chrome",
    #         "options": chrome_options
    #     }
    # else:
    #     password = base.read_admin_password()
    #     if password == False:
    #         sys.exit(1)
    browser = "chrome"
    test_path, report = base.choice_test_model(product)
    if test_path == False:
        sys.exit(1)
    seldom.main(
        path=test_path,
        report=report,
        title="蓝鲸UI自动化",
        browser=browser,
        timeout=10,
        debug=False
    )







