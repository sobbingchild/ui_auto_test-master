import requests
import json
from pre_data.obtain_token import ObtainToken
from bk_job.base_operate import BaseOperate
from bk_job import settings

ObtainToken = ObtainToken()
BaseOperate = BaseOperate()

username = settings.USER_NAME
passwd = BaseOperate.read_data(key='passwd')
#passwd = settings.PASSWORD
url = BaseOperate.read_data(key=settings.URL_LOGIN)
web_url = BaseOperate.read_data(key=settings.JOB_API_URL)
header = ObtainToken.join_headers(username, passwd, url, web_url, False)


class JobApi():
    def get_hosts_ip(self):
        """IP选择器根据拓扑节点集合获取机器列表,返回第一台机器IP"""
        add_case = web_url + "/job-manage/web/scope/biz/2/topology/hosts/nodes"
        # payload = {"appTopoNodeList": [{"objectId": "biz", "instanceId": 2}],
        #            "agentStatus": "", "searchContent": "", "pageSize": 13, "start": 0}
        payload = {"appTopoNodeList": [{"objectId": "biz", "instanceId": "2"}], "agentStatus": "", "searchContent": "",
                   "pageSize": 12, "start": 0}
        response = requests.post(add_case, data=json.dumps(payload), headers=header)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                linux_ip, windows_ip = ObtainToken.get_ip_alive(response['data']['data'])
                ObtainToken.write_config("ui_ip", linux_ip[0])
                return linux_ip
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def add_task_template(self, taskname):
        """创建作业模板"""
        add_case = web_url + "/job-manage/web/scope/biz/2/task/template/0"
        payload = {"name": taskname, "tags": [], "variables": [
            {"id": -3, "name": "count_one", "type": 1, "defaultValue": "", "defaultTargetValue": {
                "variable": "", "hostNodeInfo": {"ipList": [], "dynamicGroupList": [], "topoNodeList": []}},
             "description": "", "changeable": 0, "required": 0, "delete": 0, "value": "",
             "targetValue": {
                 "variable": "", "hostNodeInfo": {"ipList": [], "dynamicGroupList": [], "topoNodeList": []}}}],
                   "steps": [
                       {"id": 0, "name": "步骤执行脚本_test", "type": 1, "delete": 0, "enable": 0, "approvalStepInfo": {},
                        "fileStepInfo": {}, "scriptStepInfo": {
                           "scriptId": "", "ignoreError": 0, "scriptParam": "", "timeout": 7200, "scriptSource": 1,
                           "scriptVersionId": "", "secureParam": 0, "content":
                               "IyEvYmluL2Jhc2gKCmFueW5vd3RpbWU9ImRhdGUgKyclWS0lbS0lZCAlSDolTTolUyciCk5PVz0iZWNoby"
                               "BbXGAkYW55bm93dGltZVxgXVtQSUQ6JCRdIgoKIyMjIyMg5Y+v5Zyo6I"
                               "Sa5pys5byA5aeL6L+Q6KGM5pe26LCD55So77yM5omT5Y2w5b2T5pe255qE5pe26Ze05oiz5Y+KUElE44CC"
                               "CmZ1bmN0aW9uIGpvYl9zdGFydAp7CiAgICBlY2hvICJgZXZhbCAkTk9X"
                               "YCBqb2Jfc3RhcnQiCn0KCiMjIyMjIOWPr+WcqOiEmuacrOaJp+ihjOaIkOWKn+eahOmAu+i+keWIhuaUr+"
                               "WkhOiwg+eUqO+8jOaJk+WNsOW9k+aXtueahOaXtumXtOaIs+WPilBJROO"
                               "AgiAKZnVuY3Rpb24gam9iX3N1Y2Nlc3MKewogICAgTVNHPSIkKiIKICAgIGVjaG8gImBldmFsICROT1dgI"
                               "GpvYl9zdWNjZXNzOlskTVNHXSIKICAgIGV4aXQgMAp9CgojIyMjIyDlj6/ln"
                               "KjohJrmnKzmiafooYzlpLHotKXnmoTpgLvovpHliIbmlK/lpITosIPnlKjvvIzmiZPljbDlvZPml7bnmoT"
                               "ml7bpl7TmiLPlj4pQSUTjgIIKZnVuY3Rpb24gam9iX2ZhaWwKewogICAgTVN"
                               "HPSIkKiIKICAgIGVjaG8gImBldmFsICROT1dgIGpvYl9mYWlsOlskTVNHXSIKICAgIGV4aXQgMQp9Cm1rZ"
                               "GlyIC1wIC90bXAvdGVzdC8Kam9iX3N0YXJ0CgojIyMjIyMg5L2c5Lia5bmz5"
                               "Y+w5Lit5omn6KGM6ISa5pys5oiQ5Yqf5ZKM5aSx6LSl55qE5qCH5YeG5Y+q5Y+W5Yaz5LqO6ISa5pys5py"
                               "A5ZCO5LiA5p2h5omn6KGM6K+t5Y+l55qE6L+U5Zue5YC8CiMjIyMjIyDlpo"
                               "Lmnpzov5Tlm57lgLzkuLow77yM5YiZ6K6k5Li65q2k6ISa5pys5omn6KGM5oiQ5Yqf77yM5aaC5p6c6Z2e"
                               "MO+8jOWImeiupOS4uuiEmuacrOaJp+ihjOWksei0pQojIyMjIyMg5Y+v5"
                               "Zyo5q2k5aSE5byA5aeL57yW5YaZ5oKo55qE6ISa5pys6YC76L6R5Luj56CBCgo=",
                           "scriptLanguage": 4, "account": 3, "status": 0, "executeTarget": {
                               "variable": "", "hostNodeInfo": {"ipList": [
                                   {"ip": ObtainToken.read_config('ui_ip'), "cloudAreaInfo": {
                                       "id": 0}, "realId": "0:" + ObtainToken.read_config('ui_ip')}],
                                   "dynamicGroupList": [], "topoNodeList": []}}},
                        "localValidator": True}], "description": ""}
        response = requests.put(add_case, data=json.dumps(payload), headers=header)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                ObtainToken.write_config("template_id_int", response['data'])
                return response['data']
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def find_task_template(self, template_id):
        """查询作业模板详情"""
        add_case = web_url + "/job-manage/web/scope/biz/2/task/template/" + str(template_id)
        payload = {"appId": 2, "username": "admin"}
        response = requests.get(add_case, params=payload, headers=header, timeout=10)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                return response['data']['variableList'][0]['id'], response['data']['stepList'][0]['id']
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def add_task_plan(self, planname, template_id):
        """新建执行方案"""
        add_case = web_url + "/job-manage/web/scope/biz/2/task/plan/" + str(template_id) + "/0"
        variable_id, enableSteps = self.find_task_template(template_id)
        payload = {"name": planname, "enableSteps": [enableSteps], "variables": [{
            "id": variable_id, "name": "count_one", "type": 1, "defaultValue": "", "defaultTargetValue": {
                "variable": "", "hostNodeInfo": {
                    "ipList": [], "dynamicGroupList": [], "topoNodeList": []}},
            "description": "", "changeable": 0, "required": 0, "delete": 0, "value": "", "targetValue": {
                "variable": "", "hostNodeInfo": {"ipList": [], "dynamicGroupList": [], "topoNodeList": []}}}]}
        response = requests.put(add_case, data=json.dumps(payload), headers=header, timeout=10)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                ObtainToken.write_config("plan_id_int", response['data'])
                ObtainToken.write_config("steps_id_int", enableSteps)
                return response['data']
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))

    def add_task(self, tempname, planname):
        """根据tempname：模板名称，planname：执行方案名称 创建作业模板及执行方案"""
        template_id = self.add_task_template(tempname)
        plan_id = self.add_task_plan(planname, template_id)
        return template_id, plan_id

    # def del_task_plan(self):
    #     """删除执行方案"""
    #     add_case = web_url + "/job-manage/web/scope/biz/2/task/plan/" + \
    #                str(ObtainToken.read_config('steps_id_int')) \
    #                + "/" + str(ObtainToken.read_config('plan_id_int'))
    #     payload = {}
    #     response = requests.delete(add_case, data=json.dumps(payload), headers=header)
    #     response = json.loads(response.text)
    #     try:
    #         if response['code'] in [0, "1500200", "00", 'OK', 200]:
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         print("请求失败{}".format(e))

    def del_template(self, template_id):
        """删除作业模板"""
        add_case = web_url + "/job-manage/web/scope/biz/2/task/template/" + str(template_id)
        payload = {}
        response = requests.delete(add_case, data=json.dumps(payload), headers=header)
        response = json.loads(response.text)
        try:
            if response['code'] in [0, "1500200", "00", 'OK', 200]:
                return True
            else:
                return False
        except Exception as e:
            print("请求失败{}".format(e))


if __name__ == "__main__":
    a = JobApi()
    linux_ip = a.get_hosts_ip()
    print(linux_ip)
    print(type(linux_ip))
    #temp_id = a.add_task(settings.TEST_JOB_CRON_TEMP,settings.TEST_JOB_CRON_TEMP)
    #print(temp_id) #(309, 1000267)
    status = a.del_template('309')
    print(status)
    # print(linux_ip)
    # aa, b = a.add_task("test", "uuu")
    # print(a.del_template(aa))
