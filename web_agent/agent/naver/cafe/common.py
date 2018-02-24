from enum import IntEnum


class Cafe:
    def __init__(self, id, name, addr):
        self.id = id
        self.name = name
        self.addr = addr


class Post:
    def __init__(self, id, title, writer, time, read, comments, postlink, commentlink):
        self.id = id
        self.title = title
        self.writer = writer
        self.time = time
        self.read = read
        self.comments = comments
        self.postlink = postlink
        self.commentlink = commentlink

    def __str__(self):
        return str(self.id) + ' ' + self.title + ' ' + '[' + str(self.comments) + ']' + ' ' + self.time + ' ' + 'read: ' + str(self.read)


class QueryType(IntEnum):
    TOP_VIEW = 1,
    TOP_COMMENT = 2


class Range(IntEnum):
    PAST_2_HOURS = 1
    PAST_4_HOURS = 2
    PAST_24_HOURS = 3
    PAST_WEEK = 4


class Field(IntEnum):
    ID = 0
    TITLE = 1
    WRITER = 2
    TIME = 3
    READ = 5


def get_cafe_page_addr(clubid, page_num):
    addr = 'http://cafe.naver.com/ArticleList.nhn'
    clubid_search = '?search.clubid=' + str(clubid)
    menu_search = '&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501'
    page_search = '&search.page=' + str(page_num)

    return addr + clubid_search + menu_search + page_search
