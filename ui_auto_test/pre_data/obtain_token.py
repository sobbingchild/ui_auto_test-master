import os
import requests
import re
import time
import string
import random
import logging
from configobj import ConfigObj

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
logging.basicConfig(level=logging.INFO, format='%(asctime)s''- %(levelname)s: %(message)s')


class ObtainToken():
    def __init__(self):
        #self.path = PATH('config.ini')
        self.path = PATH('../../config.ini')
        self.session = requests.Session()
        self.session.verify = False

    # 获取csrftoken
    def get_csrftoken(self, url, token_name):
        resp = self.session.get(url, verify=False)
        if resp.status_code == 200:
            return resp.cookies[token_name]

    # 获取登录bk_token,url为登录页面url
    def login(self, username, passwd, url):
        login_url = url + '/login/?c_url=/'
        login_csrftoken = self.get_csrftoken(login_url, 'bklogin_csrftoken')
        login_form = {
            'csrfmiddlewaretoken': login_csrftoken,
            'username': username,
            'password': passwd
        }
        resp = self.session.post(login_url, data=login_form, verify=False)
        try:
            if resp.status_code == 200:
                cookie = str(self.session.cookies)
                bktoken = re.findall(r'bk_token=[^\s]*', cookie)
                return bktoken[0]
        except Exception as e:
            print("获取token失败，请检查用户名密码是否正确！{}".format(e))

    # 获取bkuser_csrftoken，web_url为各产品首页url
    def get_bkuser_csrftoken(self, header, web_url):
        client = requests.session()
        client.get(web_url, headers=header)
        if 'bkuser_csrftoken' in client.cookies:
            csrftoken = client.cookies['bkuser_csrftoken']
            return csrftoken
        else:
            print('获取bkuser_csrftoken失败')

    # 拼接web登录需要的header, csrftoken为是否需要csrftoken，默认需要
    def join_headers(self, username, passwd, url, web_url, csrftoken=True):
        header = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/94.0.4606.61 Safari/537.36"
        }
        cookie = self.login(username, passwd, url)
        header['Cookie'] = cookie
        if csrftoken is True:
            csrftoken = self.get_bkuser_csrftoken(header, web_url)
            header['Cookie'] = cookie + ";" + "bkuser_csrftoken=" + csrftoken
            header['X-CSRFToken'] = csrftoken
        return header

        # 写对应数据到config配置文件

    def write_config(self, key, value):
        config = ConfigObj(self.path, encoding='UTF-8')
        # config.read(self.config_path)
        # 判断参数是否为int
        if "int" in key:
            value = str(value)
        config["userdata"][key] = value
        config.write()

    # 读取config配置文件中指定数据
    def read_config(self, key):
        config = ConfigObj(self.path, encoding='UTF-8')
        try:
            value = config["userdata"][key]
            return value
        except:
            print("配置文件没有找到{}".format(key))

    # 随机生成一个字符串
    def random_data(self):
        data = str(int(time.time()))
        data = data[5:]
        random_char = random.choice(string.ascii_lowercase)
        random_char1 = random.choice(string.ascii_lowercase)
        random_str = random_char + data + random_char1
        return random_str

    # 查找安装agent的 Windows IP 和Linux IP
    def get_ip_alive(self, reprose):
        linux_ip = []
        windows_ip = []
        for r in reprose:
            if r['alive'] == 1:
                if 'linux' in r['os']:
                    linux_ip.append(r['ip'])
                else:
                    windows_ip.append(r['ip'])
        return linux_ip, windows_ip