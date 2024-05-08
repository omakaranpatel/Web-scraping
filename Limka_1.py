import scrapy


class LimkaSpider(scrapy.Spider):
    name = "Limka"
    allowed_domains = ["www.www1.homelife.ca"]
    start_urls = ["https://www.www1.homelife.ca/node/596756"]

    def parse(self, response):
        print( "[ PARSE ]" )
        Profile_pic=response.css(".agentimg img::attr(src)").get() 
        Name=response.css(".title-wrapper h2 ::text").get() 
        Role=response.css(".title-wrapper h3::text").get()
        Direct= response.css('.nwp ::text').getall()[0]
        Company=response.css(".nwp::text").getall()[1]
        Website=response.css('dd a::attr(href)').getall()
        locality=response.css('.detail-item p font::text').getall()
        Language=response.css('.detail-item.lastitem p::text').getall()
        

        yield{
            'Agent_Image':Profile_pic,
            'Agent_Name':Name,
            'Role':Role,
            'Direct':Direct,
            'Office_1':Company,
            'Agent_website':Website,
            'Locations':locality,
            'Languages':Language,
            

        }

