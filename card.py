import time
import logging
import yagmail
from json import loads as json_loads
from os import path as os_path
from sys import exit as sys_exit

from lxml import etree
from requests import session
import requests
class SoCloud:
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"

    # 初始化会话
    def __init__(self,
                 uid, psw,
                 url_login='https://5socloud.gq/auth/login'):
        """
        初始化一个session，及登录信息
        :param uid: 账号
        :param psw: 密码
        :param url_login: 登录页，默认服务为空
        """
        self.session = session()
        self.session.headers['user-agent'] = self.UA
        self.url_login = url_login

        self.uid = uid
        self.psw = psw
    
    def _page_init(self):
        init_url = "https://5socloud.gq/user"
        
        headers = {
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "User-Agent": self.UA
        }
        
        page = self.session.get(init_url,headers=headers)
        
        if page.status_code == 200:
            print("Initial page success!")
        else:
            print("Failed to open initial page!")
        login_page =  self.session.get(self.url_login,headers=headers)
        if login_page.status_code == 200:
            print("Initial login page success!")
        else:
            print("Failed to open initial login page!")

    def login(self):

        self._page_init()
        data = {
            "email":self.uid,
            "password":self.psw,
            "code":''
        }

        headers = {
            "Origin"    : "https://5socloud.gq",
            "Referer"   : self.url_login,
            "User-Agent": self.UA
        }

        post = self.session.post(
                self.url_login,
                data=data,
                headers=headers,
                allow_redirects=False)
        print(post)
        # 抓包post无法载入返回信息

        #print(self.session.cookies.get_dict())
        
        #cookies = requests.utils.dict_from_cookiejar(response.cookies)
        #print(cookies)
        log_url = "https://5socloud.gq/user/trafficlog"
        traffic = self.session.get(log_url)
        print(traffic)
        # 抓包traffic返回信息好像是个js文件...大概这就是签到失败的原因？
        
    def checkin(self):
        headers = {
            "Origin"    : "https://5socloud.gq",
            "Referer"   : "https://5socloud.gq/user",
            "User-Agent": self.UA
        }
        
       
        post_url = "https://5socloud.gq/user/checkin"
        save = self.session.post(url=post_url,headers = headers,allow_redirects=False)
        #save_msg = json_loads(save.text)["msg"]
        print(save)
        
    def logout(self):
        
        headers = {
            "Referer"   : "https://5socloud.gq/user",
            "User-Agent": self.UA
        }

        get_url = "https://5socloud.gq/user/logout"
        bye = self.session.get(url=get_url, headers=headers)
        print(bye)
if __name__ == "__main__":
    uid = "xxx"
    psw = "yyyy"
    daily_vpn = SoCloud(uid,psw)
    daily_vpn.login()   
    #daily_vpn.checkin() 
    daily_vpn.logout()