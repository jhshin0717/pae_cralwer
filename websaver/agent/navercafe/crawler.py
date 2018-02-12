from selenium import webdriver


class Crawler:
    def __init__(self, uid, pw, cid):
        self.uid = uid
        self.pw = pw
        self.cid = cid

    def set_web_driver(self, driver_type, driver_path):
        self.driver_type = driver_type
        self.driver_path = driver_path

    def run(self, duration):
        self.__init_driver()
        self.__login()
        self.__parse()

    def __init_driver(self):
        if self.driver_type.lower() == 'chrome':
            self.driver = webdriver.Chrome(self.driver_path)
            self.driver.implicitly_wait(3)

    def __login(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys(self.uid)
        self.driver.find_element_by_name('pw').send_keys(self.pw)
        self.driver.find_element_by_css_selector(
            '#frmNIDLogin > fieldset > input').click()

    def __parse(self):
        self.driver.get()
