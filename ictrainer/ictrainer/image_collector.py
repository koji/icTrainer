from icrawler.builtin import GoogleImageCrawler
import os

class ImageCollector():

    def __init__(self, search_keyword, search_number):
        self.keyword = search_keyword
        self.number = search_number

    def get_images(self):
        if not os.path.isdir('dataset/' + self.keyword):
            os.makedirs('dataset/' + self.keyword)

        crawler = GoogleImageCrawler(storage = {"root_dir" : 'dataset/' + self.keyword})
        crawler.crawl(keyword = self.keyword, max_num = self.number)