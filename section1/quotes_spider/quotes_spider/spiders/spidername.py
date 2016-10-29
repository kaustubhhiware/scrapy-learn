# -*- coding: utf-8 -*-
import scrapy


class SpidernameSpider(scrapy.Spider):
    name = "spidername"# name has to be unique in a project duhh!
    allowed_domains = ["http://quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
       #print "+--- Extracted title : \n\n"
        #print h1_tag
        #print "\n\n"

        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
       #print "+--- Top 10 tags : \n\n"
        #print tags
        #print "\n\n"
       
        # now extract data using yield
        yield{'Title':h1_tag, 'Tags': tags}

