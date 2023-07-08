from utils.Crawler import Crawler
from utils.Formatter import Formatter

class Processor:
    '''
    Class to process the crawler and the formatter
    '''
    def __init__(self, url, depth, headers, input_type, payload, other_function: callable = None):
        self.url            = url # list of URL to be injected
        self.depth          = depth # depth of the crawler
        self.headers        = headers # headers of the request
        self.input_type     = input_type # type of the input to be injected
        self.payload        = payload # payload to be injected
        self.other_function = other_function # other function to be called after the injection if there is some process to do

    def process(self):
        '''
        Process the crawler and the formatter
        '''
        crawler = Crawler(base_url=self.url, max_depth=self.depth, headers=self.headers)
        url_list = crawler.process()

        formatter = Formatter(url_list=url_list, headers=self.headers, input_type=self.input_type, payload=self.payload, other_function=self.other_function)
        formatter.process()