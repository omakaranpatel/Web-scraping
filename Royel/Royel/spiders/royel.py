import scrapy


class RoyelSpider(scrapy.Spider):
    name = "royel"
    allowed_domains = ["www.royallepage.ca"]
    start_urls = ["https://www.royallepage.ca/en/office/ontario/whitby/royal-lepage-terrequity-realty/7498/"]

    def parse(self, response):
        print( '[ PARSE ]' )
        agent_office_name = ' '.join(response.css("h2::text").getall()).strip()[:41]
        agent_address = response.css(".card address p::text").get().strip()      
        agent_zip = response.css(".card address p::text").get().split(",")[3]    
        agent_office = response.css(".col-md-1-1 a::attr(href)").getall()[0]
        agent_office_fax = response.css(".highlight ::text").get() 
        agent_office_email = response.css(".col-md-1-1 a::attr(href)").getall()[1]
        agent_office_website = response.css(".col-im-2-3 a::attr(href)").getall()[0] 
    

        yield{
           "agent_office_name":agent_office_name,
           "agent_address":agent_address,
           "agent_zip":agent_zip.strip(),
           "agent_office":agent_office,
           "agent_office_fax ":agent_office_fax,
           "agent_office_email":agent_office_email,
           "agent_office_websites":agent_office_website,
        
        } 
