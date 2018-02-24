from agent.naver import login
from agent.naver.user import Account
from .celenium import parser
from agent import driver_util

def run_with_celenium(account, cid):
    login.login_by_webdriver(account.id, account.pw)
    posts = parser.get_posts(cid)
    driver_util.close_driver()

