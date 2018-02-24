from selenium import webdriver
from agent import settings


class Driver:
    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance == None:
            cls.__instance = Driver(
                settings.DRIVER_CONFIG['TYPE'], settings.DRIVER_CONFIG['PATH'])
        return cls.__instance.web_driver

    def __init__(self, driver_type, driver_path):
        self.web_driver = self.__load(driver_type, driver_path)

    def __load(self, driver_type, driver_path):
        # return DRIVER_LIST[driver_type](driver_path)
        return get_chrome_headless_driver(driver_path)

    @classmethod
    def close(cls):
        if cls.__instance is not None:
            cls.__instance.web_driver.close()


def get_driver():
    return Driver.instance()


def close_driver():
    return Driver.close()


def get_chrome_driver(driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(3)
    return driver


def get_chrome_headless_driver(driver_path):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    driver.implicitly_wait(3)
    return driver


DRIVER_LIST = {
    "Chrome": get_chrome_driver,
    "Chrome_Headless": get_chrome_headless_driver
}
