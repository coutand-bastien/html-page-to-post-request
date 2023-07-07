from utils.Crawler import Crawler
from utils.Formatter import Formatter

class Processor:
    def __init__(self, url, depth, headers, input_type, payload):
        self.url     = url
        self.depth   = depth
        self.headers = headers
        self.input_type = input_type
        self.payload = payload

    def process(self):
        '''
        Process the crawler

        Returns:
            str: HTML code to be injected
        '''
        crawler = Crawler(base_url=self.url, max_depth=self.depth, headers=self.headers)
        url_list = crawler.process()

        formatter = Formatter(url_list=url_list, headers=self.headers, input_type=self.input_type, payload=self.payload)
        formatter.process()