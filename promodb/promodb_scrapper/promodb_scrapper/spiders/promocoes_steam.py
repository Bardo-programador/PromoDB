import scrapy
import promodb.promodb_scrapper.setup
from promodb.promodb_scrapper.promodb_scrapper.items import PromodbScrapperItem
from promodb_api.models import Jogo
from twisted.internet.threads import deferToThread


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

        for page in self.pages:
            yield scrapy.Request(page, callback=self.async_to_sync)



    def parse_info_game(self, response):
        lista_jogos = self.extrai_lista_jogos(response)
        item = PromodbScrapperItem()
        for jogo in lista_jogos:
            jogo_steam = self.coleta_infos(jogo, item)
            print(jogo_steam)
            if not Jogo.objects.filter(nome=jogo_steam['nome'], loja="Steam").exists():
                Jogo.objects.create(**jogo_steam)


    def async_to_sync(self, response):
        return deferToThread(self.parse_info_game, response)

    def extrai_lista_jogos(self, response):
        return response.css("#search_resultsRows > a")

    def coleta_infos(self, response, item):
        item['link'] = response.xpath('@href').get()
        item['nome'] = response.css('div.responsive_search_name_combined > div.col.search_name.ellipsis > span::text').get()
        item['loja'] = 'Steam'
        item['preco'] = float(response.css("div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow::attr(data-price-final)").get()) / 100
        return item




