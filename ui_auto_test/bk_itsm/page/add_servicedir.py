# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     servicedir
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""
from bk_itsm import settings

##path需要重新写 更改为最新的，前端已更新
project = "//a[@data-test-id='navigation-router-navRouter-project']"
nav_service_dir = "//a[@data-test-id='navigation-menu-serviceDirectory']"
root_dir_more = '//div[@title="根目录"]/../i'
root_dir_add = '//div[@class="bk-tree-more"]/ul/li[1]'

service_name = "//div[@class='bk-form-content']//div[@class='bk-input-text']/input"
service_comfirm = '//div[@class="bk-dialog-wrapper"]/div/div/div[4]/div/button[1]'

#点击新增的服务目录

service_new_dir= '//div[@title="test_ui_dir"]/../i'

#移除服务

remove_flow= '//div[@class="bk-tree-more"]/ul/li[3]'



#搜索服务目录



# 删除服务目录

service_dir_more = "//span[@title='{}']/../../div[@class='tree-node']/i".format(settings.SERVICE_DIR)

service_del = "//div[@class='bk-tree-more']/ul/li[3]"

service_del_comfirm = '//div[@class="bk-dialog-wrapper"]/div/div/div[5]/div/button[1]'


