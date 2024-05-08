import scrapy


class LimcaSpider(scrapy.Spider):
    name = "limca"
    allowed_domains = ["www.www1.homelife.ca"]
    start_urls = ["https://www.www1.homelife.ca/node/707024"]

    def parse(self, response):
        print(" [ PARSE ] ")
        office_1=response.css(".nwp ::text").get() 
        office_name=response.css(".item2 h2 ::text").getall() 
        Address= response.css('.item2 p::text').getall()[0:3]
        Zip=response.css(".info_apd::text").getall()
        about=response.css(".about-wrapper p::text").get()
       

        yield{
            'office_1':office_1,
            'office_Name':office_name,
            'Address':Address,
            'Zip':Zip,
            'about':about,
           
            

        }
