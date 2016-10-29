# scrapy-learn

 A repo for learning Scrapy

You can learn it too in an hour ! Follow this [free course on Udemy](https://www.udemy.com/scrapy-web-scraping-with-python/)

## Installation

 Scrapy works on python 2.7 and 3.3 on Linux-based/MAC .

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">pip install Scrapy</pre>

Start a project with

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">scrapy startproject quotes_spider
cd quotes_spider
spider genspider spidername http://quotes.toscrape.com</pre>

This creates a file spiders/spidername.py.Also verify if the url in spidername.py is valid.If not change it. Now we shall extract some data from the website

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">scrapy crawl spidername</pre>

which generates an output similiar to spidername.out .

change line number 22 in setting.py to

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">ROBOTSTXT_OBEY = False</pre>

and rerun it to get spidername_1.out. The following line implies a successful run.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">2016-10-29 20:19:52 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)
</pre>

Let us explore _scrapy shell_ now.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">scrapy shell
In [1]: fetch('http://quotes.toscrape.com/')
2016-10-29 20:54:03 [scrapy] INFO: Spider opened
2016-10-29 20:54:05 [scrapy] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)</pre>

**response.body **shows the html code.

**view(response)** opens the page in browser.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [2]: response
Out[2]: <200 http://quotes.toscrape.com/></pre>

Let us try extracting the title of this page.Inspecting the title on [website](http://quotes.toscrape.com/),the title is the only one in **h1  **font.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [3]: response.css('h1')
Out[3]: [<Selector xpath=u'descendant-or-self::h1' data=u'<h1>\n                    <a href="/" sty'>]</pre>

_response.css('h1').extract()_ gives us the tag in html.

u' stands for unicode.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [4]: response.xpath('//h1/a/text()').extract()
Out[4]: [u'Quotes to Scrape']</pre>

we can use this to extract the title by inserting this in our parse method in spidername.py .

* * *

Let us now proceed to extract the top ten tags on the page.

Upon inspection, the tags have a class _tag-item_ so we will try extracting that first.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [5]: response.xpath('//*[@class="tag-item"]')
Out[5]: 
[<Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data=u'<span class="tag-item">\n            <a c'>]
</pre>

Now that we have the tag-item class, we shall extract the tag names

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [6]: response.xpath('//*[@class="tag-item"]/a/text()')
Out[6]: 
[<Selector xpath='//*[@class="tag-item"]/a/text()' data=u'love'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'inspirational'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'life'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'humor'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'books'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'reading'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'friendship'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'friends'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'truth'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data=u'attributed-no-source'>]</pre>

_response.xpath('//*[@class="tag-item"]/a/text()').extract()_ gives us the desired list.

This output is saved in spidername_3.out

* * *

* * *

## Section 2

Let us now proceed to extracting quotes ( finally !)

Each quote belongs to the class _quote _

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [7]: quotes = response.xpath('//*[@class="quote"]')
In [8]: first = quotes[0]
In [9]: first
Out[9]: <Selector xpath='//*[@class="quote"]' data=u'<div class="quote" itemscope itemtype="h'>
</pre>

Extract the quote part from first quote

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [10]: first.xpath('.//*[@class="text"]/text()')
Out[10]: [<Selector xpath='.//*[@class="text"]/text()' data=u'\u201cThe world as we have created it is a pr'>]</pre>

Try to extract all quotes from the page.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [11]: first.xpath('//*[@class="text"]/text()')
Out[11]: 
[<Selector xpath='//*[@class="text"]/text()' data=u'\u201cThe world as we have created it is a pr'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cIt is our choices, Harry, that show wha'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cThere are only two ways to live your li'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cThe person, be it gentleman or lady, wh'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cImperfection is beauty, madness is geni'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cTry not to become a man of success. Rat'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cIt is better to be hated for what you a'>,
 <Selector xpath='//*[@class="text"]/text()' data=u"\u201cI have not failed. I've just found 10,0">,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cA woman is like a tea bag; you never kn'>,
 <Selector xpath='//*[@class="text"]/text()' data=u'\u201cA day without sunshine is like, you kno'>]
</pre>

Notice that the author part has **itemprop=author**so extract that.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [12]: first.xpath('.//*[@itemprop="author"]/text()').extract_first()
Out[12]: u'Albert Einstein'
</pre>

To extract the linked tags, we need to extract **itemprop=keywords  **and **class=tag.**

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [13]: first.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
Out[13]: u'change,deep-thoughts,thinking,world'
In [14]: first.xpath('.//*[@class="tag"]/text()')
Out[14]: 
[<Selector xpath='.//*[@class="tag"]/text()' data=u'change'>,
 <Selector xpath='.//*[@class="tag"]/text()' data=u'deep-thoughts'>,
 <Selector xpath='.//*[@class="tag"]/text()' data=u'thinking'>,
 <Selector xpath='.//*[@class="tag"]/text()' data=u'world'>]
</pre>

The new outpu is stored in spidername_4.out .

* * *

What we have done so far is extracted the quotes from the first page . _What if,_ we desired to see quotes from subsequent pages ?  
For this we will need the next button's url. Upon inspection , it belongs to **class=next **.

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">In [15]: response.xpath('//*[@class="next"]/a/@href').extract_first()
Out[15]: u'/page/2/'
</pre>

The output for this stage is looged in spidername_5.out. 

However this data displays lists, not only the data .So execute it as 

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">scrapy crawl spidername -o quotes.csv</pre>

You might as well save it in .json or .xml format.

* * *

* * *

## Section 3

Let us go through items.py now.

Define _h1_tag_ and _tags_from section 1 as fields similiar to the comments.

We will use itemLoader to load fields into our spider.

This is how our spider looks at this stage :

<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">

<pre># -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

class SpidernameSpider(Spider):
    name = 'spidername'# name has to be unique in a project duhh!
    allowed_domains = ['http://quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(),response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag',h1_tag)
        l.add_value('tags',tags)

        return l.load_item()
</pre>

</div>

This helps identify tags individually, different from our previous attempts .The output can be viewed at spidername_6.out.

Let us take a look at pipelines.py

Edit _process_item_ to process header differently by adding the following snippet :

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">    def process_item(self, item, spider):
        if item['h1_tag']:
            item['h1_tag'] = item['h1_tag'][0].upper()
        return item 
</pre>

Also uncomment ITEM_PIPELINES in settings.py or simply add this snippet : 

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">ITEM_PIPELINES = {
    'quotes_spider.pipelines.QuotesSpiderPipeline': 300,
}</pre>

The output is stored in spidername_7.out

Instead of changing the settings globally, you may temporarily run the spider as

<pre style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">scrapy crawl spidername -s DOWNLOAD_DELAY = 3 </pre>