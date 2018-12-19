import scrapy
import re

class QuotesSpider(scrapy.Spider):
  name = "trails"

  def start_requests(self):
    urls = [
    'https://trailhead.com/me/jameldjackson',
    'https://trailhead.com/me/tmartin357',
    'https://trailhead.com/me/BabatundeAborisade',
    'https://trailhead.com/me/adhunter',
    'https://trailhead.com/me/cyndiewandia',
    'https://trailhead.com/me/jaroper86'
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    name = response.xpath('//html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[1]').extract_first()
    print(name)
    matchObj = re.match( '.*full_name":"(.*)","work.*', name)
    name = matchObj.group(1)

    # myurl = '<a href="'+response.request.url+'">Link</a>'
    myurl = response.request.url
    yield {
      'name': name,
      'badges': int(response.xpath('/html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[2]/div/div[1]/div[2]/text()').extract_first().replace(',', '')),
      'points': int(response.xpath('/html/body/div[1]/main/div/div/div/div[1]/section/div[2]/div[2]/div/div[2]/div[2]/text()').extract_first().replace(',', '')),
      'url': str(myurl)
    }
