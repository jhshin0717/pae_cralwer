from agent.naver.cafe import crawler
from agent.naver.user import Account

account = Account("mot81mjh", "na8350")
# dieselMania - 11262350
crawler.run_with_celenium(account, "11262350")



