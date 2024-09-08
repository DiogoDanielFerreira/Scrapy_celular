import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/celular"]

    def parse(self, response):

        products = response.css('div.ui-search-result__content-wrapper')

        for product in products:
            
            yield {
                
                'brand': product.css('h2.ui-search-item__title::text').get()
            }
