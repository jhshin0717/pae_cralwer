from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
# TODO: Headless Crawling
# https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/

# TODO: Path should be coming from outside.
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
# TODO: Id and Pw should be coming from outside.
driver.find_element_by_name('id').send_keys('mot81mjh')
driver.find_element_by_name('pw').send_keys('na8350')
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
# TODO: Cafe address should be coming from outside.
# TODO: Post address should be coming from outside.

page_addr = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=11262350&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501&search.page=1'
driver.get(page_addr)
iframe_element = driver.find_element_by_css_selector('#cafe_main')
driver.switch_to_frame(iframe_element)
html = driver.page_source
soup = bs(html, 'html.parser')

posts = soup.select('#main-area > div > form > table > tbody > tr')
IDX_ID = 0
IDX_TITLE = 1
IDX_WRITER = 2
IDX_TIME = 3
IDX_READ = 4
IDX_LIKE = 5
count = 0
for post in posts:    
    tds = post.findAll('td', recursive=False)
    post_id = tds[IDX_ID].text.strip()
    if len(post_id) == 0:
        continue
    post_a_list = tds[IDX_TITLE].findAll('a')
    post_link = post_a_list[0].get('href')
    post_title = post_a_list[0].text.strip()
    post_num_comment = post_a_list[1].text.strip(
        "[]") if len(post_a_list) > 1 else 0
    post_time = tds[IDX_TIME].text.strip()
    post_read = tds[IDX_LIKE].text.strip()
    count += 1
    print('count:' + str(count) + ' ' + post_id + ' ' + post_title + ' '
          + '[' + str(post_num_comment) + ']' + ' ' + post_time + ' ' + 'read: ' + str(post_read))

driver.close()