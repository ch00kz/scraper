import requests

from bs4 import BeautifulSoup

from scraper import Scraper


class Rusal(Scraper):
    """ Scraper implentation for Rusal """

    dir_name = "rusal"
    starting_url = "http://www.rusal.ru/en/press-center/press-releases/"

    def get_article_urls(self, soup):
        """ returns urls of articles on page """
        articles_container = soup.find("div", class_="dyncont-list")
        links = articles_container.find_all("a")
        urls = ["http://www.rusal.ru{}".format(link['href']) for link in links]
        return urls

    def get_article_text(self, url):
        """ returns articles text given the url """
        article_page = requests.get(url)
        soup = BeautifulSoup(article_page.text, 'html.parser')
        article = soup.find("div", class_="b-content-content b-center")
        return article.get_text()

    def page_generator(self):
        """ yields soup for all pages with articles """
        for url in [self.starting_url]:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            yield soup


# execute scraping operations
scraper = Rusal()
scraper.scrape()
