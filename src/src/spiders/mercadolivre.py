import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/celular"]

    def parse(self, response):

        products = response.css('div.ui-search-result__content-wrapper')

        for product in products:

            prices = product.css(
                'span.andes-money-amount__fraction::text').getall()
            cents = product.css(
                'span.andes-money-amount__cents::text').getall(),

            yield {

                'brand': product.css('p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text').get(),
                'name': product.css('h2.ui-search-item__title::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'old_price_cents': prices[0] if len(prices) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'new_price_cents': prices[1] if len(prices) > 1 else None,

            }
