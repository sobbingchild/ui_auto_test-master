import os
import re
import random
import string
import logging
from product_page import settings
from configobj import ConfigObj


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
config_path = PATH("../config.ini")

class BaseOperate():
    def __init__(self):
        pass

    # 读取config配置文件中指定数据
    def read_data(self, key, sessiondata="testdata", path=config_path):
        config = ConfigObj(path, encoding='UTF-8')
        try:
            value = config[sessiondata][key]
            # 判断是否为int
            if "int" in key:
                value = int(value)
            return value
        except:
            print("配置文件没有找到{}:{}字段".format(sessiondata, key))

    # 读取config配置文件中指定数据
    def read_config_all(self, sessiondata="testdata", path=config_path):
        config = ConfigObj(path, encoding='UTF-8')
        try:
            value = config[sessiondata]
            return value
        except:
            print("配置文件没有找到{}".format(sessiondata))

    # 写对应数据到config配置文件默认写sharedata，可自定义
    def write_config(self, key, value, sessiondata="sharedata", path=config_path):
        config = ConfigObj(path, encoding='UTF-8')
        # config.read(self.config_path)
        # 判断参数是否为int
        if "int" in key:
            value = str(value)
        try:
            if config[sessiondata]:
                pass
        except:
            config[sessiondata] = {}
        config[sessiondata][key] = value
        config.write()

    # 选择引用脚本
    def format_path(self, script_name):
        script = '//div[contains(text(),"{}")]'.format(script_name)
        return script

    # 返回首页地址(key为对应的seetings中的产品url.eg:settings.SOPS_URL)
    def read_test_url(self):
        ''' 获取配置文件中的URL'''
        url = []
        for i in [settings.JOB_URL, settings.SOPS_URL, settings.CMDB_URL, settings.USER_URL, settings.URL_LOGIN,
                  settings.IAM_URL, settings.ITSM_URL, settings.MONITOR_URL, settings.PAAS_URL, settings.NODEMAN_URL]:
            url.append(self.read_data(i))
        settings.JOB_URL = url[0]
        settings.SOPS_URL = url[1]
        settings.CMDB_URL = url[2]
        settings.USER_URL = url[3]
        settings.URL_LOGIN = url[4]
        settings.IAM_URL = url[5]
        settings.ITSM_URL = url[6]
        settings.MONITOR_URL = url[7]
        settings.PAAS_URL = url[8]
        settings.NODEMAN_URL = url[9]
        if None in url:
            logging.info('无法获取对应测试环境URL,测试结束')
            return False
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

    def choice_test_model(self, product):
        if product == 'all':
            logging.info('运行全量用例')
            path = './'
            report = 'index.html'
            return path, report
        elif product in ['bk_cmdb', 'bk_iam', 'bk_itsm', 'bk_job', 'bk_log_search', 'bk_monitor', 'bk_nodeman',
                         'bk_paasv3', 'bk_sops', 'bk_user_manage']:
            logging.info('运行' + product + '用例')
            path = './' + product + '/test_dir/'
            report = product + '.html'
            return path, report
        else:
            logging.info('test_product输入的产品名称不匹配,请输入正确的关键字')
            return False, False

    '''通过os.getenv获取当前环境的变量'''
    def os_getenv(self):
        '''需要获取的环境变量名称'''
        env_names = ["BK_PAAS_APP_CODE", "BK_PAAS_APP_SECRET", "BK_PAAS_ADMIN_USERNAME", "BK_PAAS_ADMIN_PASSWORD",
                     "BK_PAAS_LOGIN_HOST", "BK_PAAS_INNER_HOST", "BK_CC_HOST", "BK_JOB_API_HOST", "BK_PAAS_PUBLIC_HOST",
                     "BK_SOPS_HOST", "BK_ITSM_HOST", "BK_USER_HOST", "BK_MONITOR_HOST", "BK_IAM_HOST",
                     "BK_JOB_HOST", "BK_NODEMAN_HOST", "BK_APIGW_HTTP_HOST", "BK_APIGW_API_HOST"]
        '''约定的写入配置文件的变量名称'''
        env_config_names = ['url_login', 'url_esb', 'url_web_api_bk_cmdb', 'url_web_api_bk_job', 'username', 'passwd',
                            'url_web_api_bk_sops', 'url_web_api_bk_itsm', 'url_web_api_bk_iam', 'url_web_api_bk_apigw',
                            'url_web_api_bk_monitorv3', 'url_web_api_bk_user_manage', 'url_web_ui_bk_job',
                            'url_web_api_bk_iam', 'public_host', 'url_web_api_bk_nodeman']
        env_values = []
        for name in env_names:
            try:
                env_values.append(os.getenv(name))
            except Exception as e:
                print(e)
        for config_name in env_config_names:
            if config_name is 'url_login':
                env = self.add_http(env_values[4])
                self.write_config(config_name, env, "testdata")
            elif config_name is 'url_esb':
                env = self.add_http(env_values[5])
                self.write_config(config_name, env, "testdata")
            elif "cmdb" in config_name:
                env = self.add_http(env_values[6])
                self.write_config(config_name, env, "testdata")
            elif "api_bk_job" in config_name:
                env = self.add_http(env_values[7])
                self.write_config(config_name, env, "testdata")
            elif config_name is "username":
                self.write_config(config_name, env_values[2], "testdata")
            elif config_name is "passwd":
                self.write_config(config_name, env_values[3], "testdata")
            elif config_name is "public_host":
                if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", env_values[4]):
                    self.write_config(config_name, env_values[8], "testdata")
            elif "sops" in config_name:
                env = self.add_http(env_values[9])
                self.write_config(config_name, env, "testdata")
            elif "itsm" in config_name:
                env = self.add_http(env_values[10])
                self.write_config(config_name, env, "testdata")
            elif "iam" in config_name:
                env = self.add_http(env_values[13])
                self.write_config(config_name, env, "testdata")
            elif "monitorv3" in config_name:
                env = self.add_http(env_values[12])
                self.write_config(config_name, env, "testdata")
            elif "bk_user_manage" in config_name:
                env = self.add_http(env_values[11])
                self.write_config(config_name, env, "testdata")
            elif "ui_bk_job" in config_name:
                env = self.add_http(env_values[14])
                self.write_config(config_name, env, "testdata")
            elif "nodeman" in config_name:
                env = self.add_http(env_values[15])
                self.write_config(config_name, env, "testdata")
            elif "bk_apigw" in config_name:
                env = self.add_http(env_values[16])
                self.write_config(config_name, env, "testdata")

        self.write_config("bk_app_code", env_values[0], "userdata")
        self.write_config("bk_app_secret", env_values[1], "userdata")
        self.write_config("bk_username", env_values[2], "userdata")

    # 随机生成一个字符串
    def random_data(self):
        random_char = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        # random_char1 = random.choice(string.ascii_lowercase)
        random_str = "uicheck" + random_char
        return random_str