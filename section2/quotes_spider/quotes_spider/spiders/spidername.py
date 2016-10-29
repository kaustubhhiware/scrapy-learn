# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class SpidernameSpider(Spider):
    name = "spidername"# name has to be unique in a project duhh!
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for each in quotes:
            # . needed for specific , not complete
            text = each.xpath('.//*[@class="text"]/text()').extract_first()
            author = each.xpath('.//*[@itemprop="author"]/text()').extract_first()
            associated_tags = each.xpath('.//*[@class="tag"]/text()').extract()

            yield{
                'Quote':text,
                'Author':author,
                'Tags' : associated_tags
            }

        # continue to next pages
        next_pg_add = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # /page2/

        next_pg_url = response.urljoin(next_pg_add)
        yield Request(next_pg_url)# this goes to 10 pages
