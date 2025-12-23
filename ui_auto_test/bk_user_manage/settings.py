

URL_LOGIN = 'url_login'
LOGIN_TITLE_ENGLISH = 'Login | Tencent BlueKing'

LOGIN_TITLE = '登录 | 腾讯蓝鲸智云'

INDEX_TITLE = '用户管理 | '

USER_URL = "url_web_api_bk_user_manage"

ENVIRONMENT = False

import random as r
import time
time_now = int(time.time())
timeArray = time.localtime(time_now)
otherStyleTime = time.strftime("%m%d%H%M%S", timeArray)

a1=['a','b','c','d','e','f','g','h','X','Z','k','O','m','P']
a2=['a','b','c','d','e','f','g','h','ii','jj','ki','ll','m','nn']
a3=['ac','b','c','d','e','f','g','h','ii','jj','k','ll','m','nn']
a4=['a','b','c','d','e','f','gu','h','ii','jj','k','ll','m','nn']
a5=['G','bw','c','d','e','f','W','h','Z','X','k','Y','m','Q']
a6=['a','b','c','d','e','fh','g','hh','ii','jj','k','ll','ml','nn']
a7=['a','bq','c','d','W','f','g','h','V','X','k','U','m','Q']
a8=['ac','b','c','d','e','f-','g','h','ii','jj','k','lnl','m','nn']
a9=['a','b','cx','d-','e','f','g','h','ii','jvj','kb','ll','m','nn']
a10=['在','啊','额','去','我','惹','她','有','哦','排','是','的','分','这',"会","里"]
for i in range(15):
   Name_1 =r.choice(a1)+r.choice(a2)+r.choice(a3)+r.choice(a4)+r.choice(a5)+r.choice(a6)+r.choice(a7)+r.choice(a8)+r.choice(a9)+otherStyleTime
   Name_2 =r.choice(a3)+r.choice(a3)+r.choice(a3)+r.choice(a1)+r.choice(a5)+r.choice(a6)+r.choice(a7)+r.choice(a8)+r.choice(a7)+otherStyleTime
   Name_3 = r.choice(a1)+r.choice(a7)+otherStyleTime+r.choice(a5)
   Name_4 = r.choice(a7) + r.choice(a1) + otherStyleTime + r.choice(a5)
   Name_5 = r.choice(a5) + r.choice(a7) + otherStyleTime + r.choice(a1)
   Child_Name = r.choice(a7) + otherStyleTime + r.choice(a1)
   Field_Name = otherStyleTime
   EN_Name = r.choice(a3)+r.choice(a3)+r.choice(a3)+r.choice(a1)+r.choice(a5)+r.choice(a6)
PullName = "6656"