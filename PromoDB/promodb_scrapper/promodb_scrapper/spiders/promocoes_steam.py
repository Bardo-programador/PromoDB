import scrapy
from promodb_scrapper.items import PromodbScrapperItem
import json
from scrapy.selector import Selector
class PromocoesSteamSpider(scrapy.Spider):
    name = "promocoes_steam"
    allowed_domains = ["store.steampowered.com"]
    start_urls = [
        "https://store.steampowered.com/search/?supportedlang=english&specials=1&hidef2p=1&ndl=1&page=1"
    ]
    pages = [start_urls[0]]
    def parse(self, response):
        # Pega os dados através de uma requisição json
        total_pages = response.xpath('//*[@id="search_result_container"]/div[4]/div[2]/a[3]/text()').get()

        for page in range(2, int(total_pages)+1):
            self.pages.append(f"https://store.steampowered.com/search/?supportedlang=english&specials=1&hidef2p=1&ndl=1&page={page}")
        print(self.pages)
        for page in self.pages:
            yield scrapy.Request(url=page, callback=self.parse_info_game)


    def parse_info_game(self, response):
        yield {
            "nome": "teste"
        }