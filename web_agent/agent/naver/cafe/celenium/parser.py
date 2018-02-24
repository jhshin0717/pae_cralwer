from agent import driver_util
from agent.naver.cafe.common import *
from bs4 import BeautifulSoup as bs
from datetime import datetime


def get_posts(clubid, query_type=QueryType.TOP_VIEW, result_num=20, duration=Range.PAST_2_HOURS):
    # get current time
    # current_dt = datetime.now
    # current_dt.strftime("%Y/%m/%d"))
    # current_dt.strftime("%H:%M:%S"))
    posts = []
    for page in range(1, 3):
        page_addr = get_cafe_page_addr(clubid, page)
        parse_page(page_addr, None, posts)

    print("post size: ", len(posts))
    return posts


def parse_page(page_addr, time, posts):
    driver = driver_util.get_driver()
    driver.get(page_addr)
    iframe_element = driver.find_element_by_css_selector('#cafe_main')

    driver.switch_to_frame(iframe_element)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    rawtitles = soup.select('#main-area > div > form > table > tbody > tr')

    for rawtitle in rawtitles:
        post = parse_post_title(rawtitle)
        if post is not None:
            posts.append(post)
            print('count: ', len(posts), " ", post)


def parse_post_title(post):
    tds = post.findAll('td', recursive=False)
    pid = tds[Field.ID].text.strip()
    if len(pid) == 0:
        return None

    post_a_list = tds[Field.TITLE].findAll('a')
    postlink = post_a_list[0].get('href')
    title = post_a_list[0].text.strip()
    comments = post_a_list[1].text.strip(
        "[]") if len(post_a_list) > 1 else 0
    time = tds[Field.TIME].text.strip()
    read = tds[Field.READ].text.strip()

    return Post(pid, title, None, time, read, comments, postlink, None)
