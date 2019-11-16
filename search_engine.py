'''
@Description: 
@Author: Wu Xie
@Github: https://github.com/shiehng
@Date: 2019-07-13 20:06:16
'''
# 构造单词列表，这些单词将被忽略
ignore_words = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])

class crawler:
    # 初始化crawler类并传入数据库名称
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def db_commit(self):
        pass
    
    # 辅助函数，用于获取条目的id，并且如果条目不存在，就将其加入数据库中
    def get_entry_id(self, table, field, value, create_new=True):
        return None

    # 为每个网页建立索引
    def add_to_index(self, url, soup):
        print("Indexing %s" % url)

    # 从一个HTML网页中提取文字（不代表标签的）
    def get_text_only(self, soup):
        return None

    # 根据任何非空白字符进行分词处理
    def separate_words(self, text):
        return None

    # 如果url已经建过索引，则返回true
    def is_indexed(self, url):
        return False

    # 添加一个关联两个网页的链接
    def add_link_ref(self, url_from, url_to, link_text):
        pass

    # 从一小组网页开始进行广度优先搜索，直至某一给定深度，
    # 期间为网页建立索引
    def crawl(self, pages, depth=1):
        import requests
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36'
        }

        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = requests.get(page, headers=headers)
                except:
                    print('Could not open %s' % page)
                    continue
                soup = BeautifulSoup(c.text, features="html.parser")
                self.add_to_index(page, soup)

                links = soup('a')
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1 : continue
                        url = url.split('#')[0] # 去掉位置部分
                        if url[0:4] == 'http' and not self.is_indexed(url):
                            newpages.add(url)
                        link_text = self.get_text_only(link)
                        self.add_link_ref(page, url, link_text)

                self.db_commit()
            pages = newpages

    # 创建数据库表
    def create_index_tables(self):
        pass
