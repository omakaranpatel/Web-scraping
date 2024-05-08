import scrapy


class AgentSpider(scrapy.Spider):
    name = "Agent"
    allowed_domains = ["www.realtyexecutives.com"]
    start_urls = ["https://www.realtyexecutives.com/agents/alysia-heun"]

    def parse(self, response):
        print("[ PARSE ]")
        Image=response.css(".profile-img div::attr(style)").get() 
        Name=response.css(".about-entity h1 span::text").get() 
        Role=response.css(".col-sm-5 p::text").getall()[0]
        Company=response.css(".col-sm-5 div::text").getall()[6]
        Address=response.css('.col-sm-5 div p::text').get().replace('\r\n','').replace('  ','').strip()
        locality=response.css('.col-sm-5 div p span::text').getall()[0]
        Region=response.css('.col-sm-5 div p span::text').getall()[1]
        Postal_code=response.css('.col-sm-5 div p span::text').getall()[2]
        Direct_phone= response.css('.col-sm-5 p span::text').getall()[3]
        Facebook=response.css(".agent-profile-social a::attr(href)").getall()[0]
        Twitter=response.css(".agent-profile-social a::attr(href)").getall()[1]
        Linkedin=response.css(".agent-profile-social a::attr(href)").getall()[2]
        Youtube=response.css(".agent-profile-social a::attr(href)").getall()[3]
        Instagram=response.css(".agent-profile-social a::attr(href)").getall()[4]
        Pinterest=response.css(".agent-profile-social a::attr(href)").getall()[5]
        Blog=response.css(".agent-profile-social a::attr(href)").getall()[6]
        Website=response.css('.about-button a::attr(href)').getall()[1]
        Language=response.css('.col-sm-12 div::text').get()[18:] 
        Bio= response.css('.bioSection p::text').getall()
        

        yield{
            'Agent_Image':Image,
            'Agent_Name':Name,
            'Role':Role,
            'Company':Company,
            'Address':Address,
            'Locality':locality,
            'Region':Region,
            'Postal_code':Postal_code,
            'Direct_no':Direct_phone,
            'Facebook':Facebook,
            'Twitter':Twitter,
            'Linkedin':Linkedin,
            'Youtube':Youtube,
            'Instagram':Instagram,
            'Pinterest':Pinterest,
            'Blog':Blog,
            'Agent_website':Website,
            'Languages':Language,
            'Agent_Bio':Bio

        }