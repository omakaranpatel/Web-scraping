import scrapy


class Limka4Spider(scrapy.Spider):
    name = "Limka_4"
    allowed_domains = ["www.homelifebc.com"]
    start_urls = ["https://www.homelifebc.com/April-Kaayk"]

    def parse(self, response):
        print(" [ PARSE ] ")
        Office_Name=response.css(".office-info.contact-details h3 ::text").get() 
        Office_1=response.css(".phone a::text").get()
        Office_2=response.css(".agent-tollfree a::text").get()
        Address=response.css('.address span::text').get()
        zip= response.css('.address span::text').get()[-7:]
        agent_facebook = response.css(".widgets-text-widget a::attr(href)").get()
        agent_Googel = response.css(".widgets-text-widget a::attr(href)").getall()[1]
        agent_instagram = response.css(".widgets-text-widget a::attr(href)").getall()[2]
        


       

        yield{
            'Office_Name':Office_Name,
            'Office_1':Office_1,
            'Office_2':Office_2,
            'Address':Address,
            'zip':zip,
            'agent_facebook':agent_facebook,
            'agent_Googel':agent_Googel,
            'agent_instagram':agent_instagram
        }


