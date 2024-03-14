import scrapy


class KdSpider(scrapy.Spider):
    name = "ram"
    start_urls = ["https://www.kw.com/agent/Sal-Sorrentino/164529","https://www.kw.com/agent/Tom-Amiss/164245","https://www.kw.com/agent/Andy-Onushco/164264","https://www.kw.com/agent/Brian-Butterfield/164355"]

    def parse(self, response):
        print('[ PARSE ]')
        data = response.css('.Page-body')
        for kw in data:

            name = kw.css('div.Agent-topcard-detail-name span ::text').get()
            Role = kw.css('div.MarketCenterContact-agentcard span.MarketCenterContact-agentinfo-subname::text').get()
            agent_photo = kw.css(".Agent-topcard-photo picture img.Image::attr(src) ").get()
            company = kw.css('div.Agent-topcard-detail-MC-name span::text').get().strip()
            location =kw.css('.MarketCenterContact-marketcenterinfo-address::text').getall()
            language =kw.css('div.Agent-details span::text').getall()
            license = kw.css('.Agent-topcard-license-bar-licenses span::text').get().strip()
            phone = kw.css('div.Agent-topcard-contact a::attr(href)').get()
            email = kw.css('.Agent-topcard-detail-link a::attr(href)').getall()[1]
            website = kw.css('.Agent-topcard-detail-link a::attr(href)').getall()
            about = kw.css('div.CollapsibleText-content.CollapsibleText--large.body-md::text').get().strip()
            office_image = kw.css('div.MarketCenterContact-container picture img.Image::attr(src)').get()
            office_locations = kw.css('.MarketCenterContact-marketcenterinfo-address ::text').get()
            office_phone = kw.css('kw-intl-phone-format::attr(data-phone-number)').get()
            FB_url = kw.css('.SocialBar-items a::attr(href)').getall()[2]
            youtube_url = kw.css('.SocialBar-items a::attr(href)').getall()[1]
            twiter_url = kw.css('.SocialBar-items a::attr(href)').get()
            instagram_url = kw.css('.SocialBar-items a::attr(href)').getall()[4]
            linkdin_url = kw.css('.SocialBar-items a::attr(href)').getall()[3]
            yield {
                'name': name,
                'Role':Role,
                'agent_photo': agent_photo,
                'company': company,
                'location': location,
                'language': language[1],
                'license' : license,
                'phone': phone,
                'email': email,
                'website': website[2],
                'about': about,
                'office_image': office_image,
                'office_locations': office_locations,
                'office_phone': office_phone,
                'FB_url':FB_url,
                'youtube_url':youtube_url,
                'twiter_url':twiter_url,
                'instagram_url':instagram_url,
                'linkdin_url':linkdin_url

            }
            data = response.css('.')
        for kw in data:

            name = kw.css('::text').get()
            Role = kw.css('::text').get()
            agent_photo = kw.css(".img.Image::attr(src) ").get()
            company = kw.css('::text').get().strip()
            location =kw.css('.::text').getall()
            language =kw.css('span::text').getall()
            license = kw.css('.::text').get().strip()
            phone = kw.css(' a::attr(href)').get()
            email = kw.css(' a::attr(href)').getall()[1]
            website = kw.css('::attr(href)').getall()
            about = kw.css('::text').get().strip()
            office_image = kw.css('img.Image::attr(src)').get()
            office_locations = kw.css('.::text').get()
            office_phone = kw.css('::attr(data-phone-number)').get()
            FB_url = kw.css('.SocialBar-items a::attr(href)').getall()[2]
            youtube_url = kw.css('.SocialBar-items a::attr(href)').getall()[1]
            twiter_url = kw.css('.SocialBar-items a::attr(href)').get()
            instagram_url = kw.css('.SocialBar-items a::attr(href)').getall()[4]
            linkdin_url = kw.css('.SocialBar-items a::attr(href)').getall()[3]
            yield {
                'name': name,
                'Role':Role,
                'agent_photo': agent_photo,
                'company': company,
                'location': location,
                'language': language[1],
                'license' : license,
                'phone': phone,
                'email': email,
                'website': website[2],
                'about': about,
                'office_image': office_image,
                'office_locations': office_locations,
                'office_phone': office_phone,
                'FB_url':FB_url,
                'youtube_url':youtube_url,
                'twiter_url':twiter_url,
                'instagram_url':instagram_url,
                'linkdin_url':linkdin_url

            }