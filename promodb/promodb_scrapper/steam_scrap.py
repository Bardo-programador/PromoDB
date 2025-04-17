from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .promodb_scrapper.spiders.promocoes_steam import PromocoesSteamSpider  # ajuste com o nome real

def rodar_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(PromocoesSteamSpider)
    process.start()