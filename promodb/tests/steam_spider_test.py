import pytest
from scrapy.http import HtmlResponse
import aiohttp
import promodb.promodb_scrapper.setup
from promodb.promodb_scrapper.promodb_scrapper.items import PromodbScrapperItem
from promodb.promodb_scrapper.promodb_scrapper.spiders.promocoes_steam import PromocoesSteamSpider


@pytest.mark.asyncio
async def test_com_rede_real():
    url = "https://store.steampowered.com/search/?supportedlang=english&specials=1&hidef2p=1&ndl=1&page=1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            assert resp.status == 200
            html = await resp.read()

    fake_response = HtmlResponse(
        url=url,
        body=html,
        encoding='utf-8'
    )

    # verifica se resposta é 200 (OK)
    assert fake_response.status == 200

    spider = PromocoesSteamSpider()
    lista = spider.extrai_lista_jogos(fake_response)

    # Validação do conteúdo
    assert len(lista) == 25, f"Esperado 25 links e retornou {len(lista)}"

    item = PromodbScrapperItem()
    for jogo in lista:
        jogo = spider.coleta_infos(jogo, item)
        # Verifica se consegue coletar informações dos jogos
        assert jogo is not None
        assert jogo["link"] is not None
        assert jogo["nome"] is not None
        assert jogo["preco"] is not None
