import scrapy
from ..items import AmazonTutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1603109482&rnid=1250225011&ref=sr_pg_1"
    ]

    def parse(self, response):
        items = AmazonTutorialItem()
        product_name = response.css(".a-color-base.a-text-normal").css("::text").extract()[0]
        product_author = response.css(".a-color-secondary .a-size-base.a-link-normal").css("::text").extract()
        product_price = response.css(".a-price-whole").css("::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items["product_name"] = product_name
        items["product_author"] = product_author
        items["product_price"] = product_price
        items["product_imagelink"] = product_imagelink

        yield items

