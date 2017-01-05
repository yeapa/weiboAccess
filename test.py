

# coding:utf-8
##http://blog.csdn.net/monsion/article/details/8115671
##https://github.com/michaelliao/sinaweibopy/wiki/OAuth2-HOWTO
from weibo import APIClient
import webbrowser  # python内置的包

APP_KEY = '1730513634'
APP_SECRET = '74fe679b5fafb1b15a303993df641eb8'
CALLBACK_URL = 'http://weibotest.com/callback.php'

# 利用官方微博SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
# 得到授权页面的url，利用webbrowser打开这个url
url = client.get_authorize_url()
print url
webbrowser.open_new(url)
# 获取code=后面的内容
print '输入url中code后面的内容后按回车键：'
code = raw_input()
# code = your.web.framework.request.get('code')
# client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in
# 设置得到的access_token
client.set_access_token(access_token, expires_in)

# 可以打印下看看里面都有什么东西
# print client.statuses__public_timeline()
statuses = client.statuses__public_timeline()['statuses']
length = len(statuses)
# 输出了部分信息
for i in range(0, length):
    print u'昵称：' + statuses[i]['user']['screen_name']
    print u'简介：' + statuses[i]['user']['description']
    print u'位置：' + statuses[i]['user']['location']
    print u'微博：' + statuses[i]['text']
