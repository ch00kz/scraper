import os
from abc import ABCMeta, abstractmethod


class Scraper(metaclass=ABCMeta):

    dir_name = ""
    starting_url = ""

    @abstractmethod
    def get_article_urls(self, soup):
        """ returns urls of articles on page """
        pass

    @abstractmethod
    def get_article_text(self, url):
        """ returns articles text given the url """
        pass

    @abstractmethod
    def page_generator(self):
        """ yields soup for all pages with articles """
        pass

    def scrape(self):
        """ runs implemented methods and scraps files """
        for soup in self.page_generator():
            for url in self.get_article_urls(soup):
                article_text = self.get_article_text(url)

                # create dir
                if not os.path.exists(self.dir_name):
                    os.makedirs(self.dir_name)

                file_name = url.split('/')[-2]  # get unique_file_name
                with open("{}/{}.txt".format(self.dir_name, file_name), "w+") as file:
                    file.write(article_text)
