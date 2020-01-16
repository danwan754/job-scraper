import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "indeed"

    start_urls = [
        'https://ca.indeed.com/jobs?q=developer&l=Vancouver%2C+BC&fromage=last'
    ]

    def parse(self, response):

        # posts = response.xpath("//div[contains(@class, 'jobsearch-SerpJobCard') and contains(@class, 'unifiedRow')]")
        
        # find the script tag containing the embedded json
        posts = re.findall("\{jk:.*\}", response.xpath('//script[@type="text/javascript"][contains(text(), "var jobmap")]/text()').get())

        for post in posts:
            post_id = re.search("(?<=\{jk:\').*(?=\',efccid)", post).group(0)
            company = re.search("(?<=cmp:\').*(?=\',cmpesc)", post).group(0)
            title = re.search("(?<=title:\').*(?=\',locid)", post).group(0)
            location = re.search("(?<=loc:\').*(?=\',country)", post).group(0)
            # date = post.xpath('./div[contains(@class, "jobsearch-SerpJobCard-footer")]//*[contains(@class, "date")]//text()').get()
            url = 'https://ca.indeed.com/viewjob?jk=' + post_id
            yield {
                'id': post_id,
                'title': title,
                'company': company,
                'location': location,
                # 'date': date,
                'url': url
            }
