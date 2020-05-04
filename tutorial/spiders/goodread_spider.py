import scrapy


class GoodSpider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'https://www.goodreads.com/quotes',
    ]
  
    def parse(self, response):
        for quote in response.css('div.quoteDetails'):
            yield {
                'image': quote.css('img').xpath('@src').get(),
                'quote': quote.css('div.quoteText::text').get(),
                'author': quote.css('div.quoteText span::text').get(),
                'tags': quote.css('div.quoteFooter div.greyText.smallText.left a::text').getall(),
                'ratings': quote.css('div.quoteFooter div.right a.smallText::text').get()
            }
        
        for a in response.css('a.next_page'):
            yield response.follow(a, callback=self.parse)


"""
    

   def start_requests(self):

    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




"""