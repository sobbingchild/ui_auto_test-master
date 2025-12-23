# -*- coding: utf-8 -*-
"""
-------------------------------------------------//tr[1]/td[7]/div/div
   File Name：     service_status.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/18
-------------------------------------------------
"""

#平台管理
navigation_publicScriptList="//div[@data-test-id='navigation_publicScriptList']"
service_status="//div[@data-test-id='navigation_service']"
job_analysis='job-analysis'
job_backup='job-backup'
job_config='job-config'
job_crontab='job-crontab'
job_execute='job-execute'
job_gateway='job-gateway'
job_logsvr='job-logsvr'
job_manage='job-manage'

line_job_analysis="//tbody/tr[1]/td[2]/div[contains(.,'{}')]".format(job_analysis)
line_job_backup="//tbody/tr[2]/td[2]/div[contains(.,'{}')]".format(job_backup)
line_job_config="//tbody/tr[3]/td[2]/div[contains(.,'{}')]".format(job_config)
line_job_crontab="//tbody/tr[4]/td[2]/div[contains(.,'{}')]".format(job_crontab)
line_job_execute="//tbody/tr[5]/td[2]/div[contains(.,'{}')]".format(job_execute)
line_job_gateway="//tbody/tr[6]/td[2]/div[contains(.,'{}')]".format(job_gateway)
line_job_logsvr="//tbody/tr[7]/td[2]/div[contains(.,'{}')]".format(job_logsvr)
line_job_manage="//tbody/tr[8]/td[2]/div[contains(.,'{}')]".format(job_manage)

status="//tbody/tr[1]/td[4]/div/span[contains(.,'正常')]"


