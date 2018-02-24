from agent import driver_util


def login_by_webdriver(id, pw):
    driver = driver_util.get_driver()
    driver.get('https://nid.naver.com/nidlogin.login')
    driver.find_element_by_name('id').send_keys(id)
    driver.find_element_by_name('pw').send_keys(pw)
    driver.find_element_by_css_selector(
        '#frmNIDLogin > fieldset > input').click()
