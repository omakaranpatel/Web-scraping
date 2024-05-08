import scrapy


class HomerealtySpider(scrapy.Spider):
    name = "homeRealty"
    allowed_domains = ["www.rightathomerealty.com"]
    start_urls = ["https://www.rightathomerealty.com/agent_find?page=8&country=&county=&city=Barrie&title=&brID1=&brID2=&brokerID=&brokerID_additional=&language=&name=&name_ajax="]

    def parse(self, response):
        print("[ PARSE ]")
        data = response.css('.agent-list-wrapper')
        for hr in data:
        
            agent_name = hr.css(".agent-summary-info a::text").get()
            agent_photo = hr.css(".agent-summary-image-wrapper img::attr(src)").get()
            agent_Role = hr.css("h4.agent_title ::text").get()
            agent_address = hr.css(".shortaddress ::text").get()
            agent_Mobile = hr.css(".mobile-phone-link::text").get()
            agent_phone = hr.css(".office-phone-link::text").get()
            agent_Zip= hr.css(".restaddress::text").get()[17:]
            #agent_instagram = response.css('.ao-social a::attr(href)').get()
            #agent_youtube = response.css(".ao-social a::attr(href)").get()
            #agent_speciality = response.css('.ao_specialties_container::text').get()
            #agent_language = response.css('.ao_languages_container::text').get()
    
    
            yield{
                "agent_name":agent_name,
               "agent_photo":agent_photo,
               "agent_Role":agent_Role,
               "agent_address":agent_address,
               "agent_Mobile":agent_Mobile,
               "agent_phone":agent_phone,
               "agent_Zip":agent_Zip,
               #"agent_linkedin":agent_linkedin,
               #"agent_instagram":agent_instagram,
               #"agent_youtube":agent_youtube,
               #"agent_speciality":agent_speciality,
               #"agent_language":  agent_language
            }                
    
    