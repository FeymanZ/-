import scrapy

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['tianqi.com']
    start_urls = ['https://www.tianqi.com/nanjing']

    def parse(self, response):
        weather_info = response.xpath('//div[@class="weatherbox"]/div[@class="left"]/ul/li')
        
        with open('weather.txt', 'w', encoding='utf-8') as f:
            for info in weather_info:
                date = info.xpath('.//h1/text()').get()
                weather = info.xpath('.//p[@class="wea"]/text()').get()
                temp = info.xpath('.//p[@class="tem"]/span/text()').get()
                temp_low = info.xpath('.//p[@class="tem"]/i/text()').get()
                wind = info.xpath('.//p[@class="win"]/span[1]/text()').get()

                f.write(f'Date: {date}, Weather: {weather}, Temperature: {temp} / {temp_low}, Wind: {wind}\n')
