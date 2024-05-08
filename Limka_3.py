import scrapy


class Limka3Spider(scrapy.Spider):
    name = "Limka_3"
    allowed_domains = ["www.homelifebc.com"]
    start_urls = ["https://www.homelifebc.com/Andrew-Janine-Hudson"]

    def parse(self, response):
        print( [ "PARSE" ] )
        Profile_pic=response.css(".agent-image img::attr(src)").get() 
        Name=response.css(".agent-name::text").get() 
        Role=response.css(".agent-title::text").get()
        Direct= response.css('.agent-contact.cell a::text').get()
        Company=response.css(".agent-contact.phone a::text").get()
        Website=response.css('.agent-contact.website a::attr(href)').get()
        locality=response.css('.agent-coverage::text').getall()
        Language=response.css('.agent-languages::text').get()
        Education=response.css('.agent-education::text').getall()[1]
        Speciality=response.css('.agent-speciality::text').get()
        Awards=response.css('.agent-awards.bio-extra::text').get()
        Experience=response.css('.agent-experience.bio-extra::text').get()
        agent_facebook = response.css(".widgets-text-widget a::attr(href)").get()
        agent_twitter = response.css(".widgets-text-widget a::attr(href)").getall()[1]
        agent_linkedin= response.css(".widgets-text-widget a::attr(href)").getall()[2]
        agent_youtube = response.css(".widgets-text-widget a::attr(href)").getall()[5]
        agent_instagram = response.css(".widgets-text-widget a::attr(href)").getall()[4]
        

        yield{
            'Agent_Image':Profile_pic,
            'Agent_Name':Name,
            'Role':Role,
            'Direct':Direct,
            'Office_1':Company,
            'Agent_website':Website,
            'Locations':locality,
            'Languages':Language,
            'Education':Education,
            'Speciality':Speciality,
            'Awards':Awards,
            'Experience':Experience,
            "agent_facebook":agent_facebook,
           "agent_twitter":agent_twitter,
           "agent_linkedin":agent_linkedin,
           "agent_youtube":agent_youtube,
           "agent_instagram ":agent_instagram
            

        }

