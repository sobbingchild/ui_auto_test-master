import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s''- %(levelname)s: %(message)s')


def get_url(url):
    if not url:
        logging.info('url为空，请检查配置文件')
        return False
    url_index = url.split('/')
    url_index = '/'.join(url_index[:-2])
    return url_index


USER_NAME = 'admin'  # 用户名

PASSWORD = 'passwd'  # 密码

ADAN_USER = "adan"

ADAN_PWD = "Bk@123456"

TIMEOUT = 10  # 检查超时时间


URL_LOGIN = 'url_login'
JOB_URL = 'url_web_bk_job'  # JOB首页
JOB_API_URL = 'url_web_api_bk_job'
SOPS_URL = 'url_web_api_bk_sops'  # 标准运维主页
# CMDB主页
CMDB_URL = 'url_web_api_bk_cmdb'
IAM_URL = 'url_web_api_bk_iam'  # IAM域名
ITSM_URL = 'url_web_api_bk_itsm'
LOG_SEARCH_URL = 'url_web_api_bk_log_search'
MONITOR_URL = 'url_web_api_bk_monitorv3'  # 监控首页
# 节点管理URL
NODEMAN_URL = 'url_web_api_bk_nodeman'
PAAS_URL = 'url_web_api_bk_passv3'
USER_URL = "url_web_api_bk_user_manage"

# 作业模板地址
JOB_TEMP_URL = get_url(JOB_URL) + '/task_manage/list'

# 定时任务地址
JOB_CRON_URL = get_url(JOB_URL) + '/cron/list?pageSize=15&start=0'

# 平台管理-地址
JOB_SCRIPT_URL = get_url(JOB_URL) + '/public_script/'

LOGIN_TITLE_ENGLISH = 'Login | Tencent BlueKing'

LOGIN_TITLE = '登录 | 腾讯蓝鲸智云'

INDEX_TITLE = '作业平台 |'
MONITOR_TITLE = '监控平台 | 蓝鲸智云'
DATA_TEST_ID = '@data-test-id'
TEST_UI_JOB_TEMP = 'TEST_UI_JOB_TEMP'
TEST_UI_NAME_QUICK = 'test_ui_name_quick'
TEST_UI_SHELL_CONTENT = 'echo test_ui_shell_content'
TEST_UI_PYTHON_CONTENT = 'print("test_ui_python_content")'

# 需依赖的执行模板与执行方案
TEST_JOB_COMMON = 'TEST_JOB_COMMON'
TEST_JOB_CRON_TEMP = 'TEST_JOB_CRON_TEMP'
COMMON_ID = ''
CRON_ID = ''
CREATE_API_STATUS = False

TEST_INPUT_IP = "10.0.15.62"

TEST_SYNC_TEXT = "echo 'test'"
TEST_PLAN_DEL_TEXT = '确定删除该执行方案？'
TEST_NAME_ACCOUNT = "test_name_account"
TEST_ALIAS_ACCOUNT = "test_alias_account"

#准入用例控制
ENVIRONMENT = False

BIZ_NAME = 'JOBUI自动化业务'

if __name__ == '__main__':
    print(JOB_TEMP_URL)
