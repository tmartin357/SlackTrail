import scrapy
import re

class QuotesSpider(scrapy.Spider):
  name = "trails"

  def start_requests(self):
    urls = [
    # 'http://quotes.toscrape.com/page/1/',
    'https://trailhead.salesforce.com/en/me/jameldjackson',
    'https://trailhead.salesforce.com/en/me/tmartin357'
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    name = response.xpath('//html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[1]').extract_first()
    print(name)
    matchObj = re.match( '.*full_name":"(.*)","work.*', name)
    name = matchObj.group(1)
    yield {
      'Name': name,
      'Badges': int(response.xpath('/html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[2]/div/div[1]/div[2]/text()').extract_first().replace(',', '')),
      'Points': int(response.xpath('/html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[2]/div/div[2]/div[2]/text()').extract_first().replace(',', ''))
    }
