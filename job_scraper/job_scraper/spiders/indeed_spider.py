import scrapy


class QuotesSpider(scrapy.Spider):
    name = "indeed"

    start_urls = [
        'https://ca.indeed.com/jobs?q=developer&l=Vancouver%2C+BC&fromage=last'
    ]

    def parse(self, response):

        posts = response.xpath("//div[contains(@class, 'jobsearch-SerpJobCard') and contains(@class, 'unifiedRow')]")

        for post in posts:
            title = post.xpath('./div[contains(@class, "title")]/a/@title').get()
            unstripped_company = post.xpath('./div[contains(@class, "sjcl")]/div/span[contains(@class, "company")]//text()').getall()
            company = ''.join(unstripped_company).strip()
            location = post.xpath('./div[contains(@class, "sjcl")]/*[contains(@class, "location")]//text()').get()
            yield {
                'title': title,
                'company': company,
                'location': location
                # 'date': 
            } 
            