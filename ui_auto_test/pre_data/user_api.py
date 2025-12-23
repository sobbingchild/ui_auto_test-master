import requests
import json
from pre_data.obtain_token import ObtainToken
from bk_user_manage.base_operate import BaseOperate
from bk_user_manage import settings

ObtainToken = ObtainToken()
BaseOperate = BaseOperate()

username = settings.USER_NAME
passwd = BaseOperate.read_data(key='passwd')
url = BaseOperate.read_data(key=settings.URL_LOGIN)
web_url = BaseOperate.read_data(key=settings.USER_URL)
header = ObtainToken.join_headers(username, passwd, url, web_url+'/accounts/login_success/')


class UserApi():

    def add_user(self):
        # api url
        add_case = web_url + "/api/v1/web/profiles/"
        # api data
        name = ObtainToken.random_data()
        payload = {"category_id": 1, "leader": [], "departments": [1],
                   "password_valid_days": 30, "username": name, "display_name": "UItest0",
                   "email": "test01@123.com", "telephone": "13123456789", "iso_code": "cn", "status": "NORMAL",
                   "staff_status": "IN", "position": 0, "wx_userid": "", "qq": ""}
        payload = json.dumps(payload)
        # 创建用户
        response = requests.post(add_case, data=payload, headers=header, timeout=10)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                # 写用户id到配置文件
                self.search_user_id(name)
                return name
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def user_passw(self):
        """重置用户密码"""
        add_case = web_url + "/api/v1/web/profiles/" + str(ObtainToken.read_config('user_id_int')) + "/"
        payload = {"password": "Blueking@654321"}
        payload = json.dumps(payload)
        response = requests.patch(add_case, data=payload, headers=header)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                return 'Blueking@654321'
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def del_user(self):
        """删除用户"""
        add_case = web_url + "/api/v1/web/profiles/batch/"
        payload = [{"id": ObtainToken.read_config('user_id_int')}]
        payload = json.dumps(payload)
        response = requests.delete(add_case, data=payload, headers=header)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                return True
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def search_user_id(self, name):
        url = web_url + "/api/v1/web/profiles/search/?category_id=1&username=" + name
        response_find = requests.get(url, headers=header, timeout=10)
        response_find = json.loads(response_find.text)
        # 写用户id到配置文件
        ObtainToken.write_config("user_id_int", response_find['data']['results'][0]['id'])

