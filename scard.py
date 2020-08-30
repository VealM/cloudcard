from selenium import webdriver

class SoCloud:
    def __init__(self, uid, psw, url_login):
        self.driver = webdriver.Chrome()
        self.uid = uid
        self.psw = psw
        self.url = url_login
    def login(self):
        self.driver.get(self.url)
        email = self.driver.find_element_by_id("email")
        email.send_keys(self.uid)
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.psw)
        self.driver.find_element_by_xpath("//*[@id='app']/section/div/div/div/div[1]/form/div/div[5]/button").click()
    def checkin(self):
        # //*[@id="checkin-div"]/a
        self.driver.find_element_by_xpath("//*[@id='checkin-div']/a").click()
        # 报错无法定位该元素 
        # 该元素信息
        # 这个checkin()就是传说中的js代码吗（js小白提问
        # <a href="#" onclick="checkin()" class="btn btn-icon icon-left btn-primary"><i class="far fa-calendar-check"></i> 每日签到</a>
        
if __name__ == "__main__":
    uid = "xxxx" 
    psw = "yyyy"
    url = "https://5socloud.gq/user"
    carder = SoCloud(uid, psw, url)
    carder.login()
    carder.checkin()        