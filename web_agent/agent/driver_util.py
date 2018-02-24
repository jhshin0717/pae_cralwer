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
        return get_chrome_driver(driver_path)


def get_driver():
    return Driver.instance()


def get_chrome_driver(driver_path):
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(3)
    return driver


DRIVER_LIST = {
    "Chrome": get_chrome_driver
}
