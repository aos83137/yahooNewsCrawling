import CrawlingModule
from KeywordModel import *


class MainCrawling():
    def __init__(self, keywords):
        if(get_keyword_list()):
            keyword_list = get_keyword_list()
            str = []
            for i, keyword in enumerate(keyword_list):
                print(keyword["keyword"])
                cm = CrawlingModule.md(keyword["keyword"])
                cm.runCrawling()
        else:
            cm = CrawlingModule.md('softbank')
            cm.runCrawling()



#밑은 그냥 테스트용 test
if (__name__ == '__main__'):
    MainCrawling('ソフトバンク')
