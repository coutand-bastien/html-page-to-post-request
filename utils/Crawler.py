from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

class Crawler:
    '''
    Crawl a web page and all pages linked to it
    '''

    def __init__(self, base_url, max_depth, headers, output=None):
        self.base_url  = urlparse(base_url) # base URL of the web page
        self.max_depth = max_depth # max depth of the crawler
        self.output    = output # output file to write the URL
        self.headers   = headers # headers of the request

        self.extensions = [
            '.js', '.png', '.jpg', '.jpeg', '.gif', '.css', '.pdf', '.doc',
            '.docx', '.svg', '.ico', '.xml', '.json', '.txt', '.mp3', '.mp4',
            '.avi', '.wmv', '.mov', '.flv', '.swf', '.zip', '.rar', '.tar',
            '.gz', '.bz2', '.7z', '.exe', '.jar', '.apk', '.iso', '.dmg',
            '.torrent', '.woff', '.woff2', '.ttf', '.otf', '.eot', '.psd',
            '.ai', '.eps', '.ps', '.xps', '.mpg', '.mpeg', '.ogg', '.mid',
            '.midi', '.wma', '.wax', '.m4a', '.m4p', '.m4b', '.m4r', '.aac',
            '.wav', '.flac', '.ape', '.wv', '.3gp', '.mkv', '.webm', '.m3u',
            '.m3u8', '.asf', '.asx', '.vob', '.m3u', '.m3u8', '.pls', '.wpl',
            '.b4s', '.xspf', '.dat', '.ifo', '.mov', '.qt', '.wmv', '.mpg',
            '.mpeg', '.avi', '.divx', '.ogm', '.mkv', '.mp4', '.m4v', '.mp4v',
            '.mpv', '.vob', '.qt', '.nsv', '.rm', '.rmvb', '.flv', '.swf',
            '.avchd', '.webm', '.html', '.htm', '.jsp', '.jspx', '.css',
            '.js', '.action', '.do', '.py', '.rb', '.xml', '.rss', '.svg',
            '.cgi', '.dll', '.jsp', '.jspx', '.pl', '.cgi', '.htaccess',
            '.htpasswd', '.bak', '.config', '.sql', '.ini', '.log', '.sh',
            '.htc', '.dat', '.inc', '.inf', '.dist', '.distz', '.inc'
        ] # list of extensions to ignore

        self.visited    = set() # set of all visited URLs

    def get_links(self, url):
        '''
        Get all links from a web page

        Args:
            url (str): URL to crawl

        Returns:
            list: List of all links found on the page
        '''
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        links = []

        for link in soup.find_all("a"):
            href = link.attrs.get("href")
            if href and not href.startswith("#") and not href.endswith(tuple(self.extensions)):
                links.append(urljoin(url, href))

        for form in soup.find_all("form"):
            action = form.attrs.get("action")
            if action and not action.startswith("#"):
                links.append(urljoin(url, action))

        return links

    def crawl(self, url, current_depth=0):
        '''
        Crawl a web page and all pages linked to it
        
        Args:
            url (str): URL to crawl
            current_depth (int, optional): Current depth of the crawl. Defaults to 0.
        '''
        if current_depth > self.max_depth:
            return

        self.visited.add(url)
        print("Crawling:", url)

        links = self.get_links(url)

        for link in links:
            if link not in self.visited:
                parsed_link = urlparse(link)
                if parsed_link.netloc == self.base_url.netloc:
                    self.crawl(link, current_depth + 1)

    def process(self):
        '''
        Process the crawler

        Returns:
            set: Set of all visited URLs
        '''
        self.crawl(self.base_url.geturl())

        if self.output:
            with open(self.output, "w") as f:
                for url in self.visited:
                    f.write(url + "\n")
                    
        return self.visited