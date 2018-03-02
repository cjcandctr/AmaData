import scrapy


class QuotesSpider(scrapy.Spider):
    name = "techSpy"

    elec_url = "https://www.amazon.com/s/ref=lp_1292110011_ex_n_1?rh=n%3A172282&bbn=172282&ie=UTF8&qid=1519961320"
    ca_selector = "#a-page > div.a-fixed-left-flipped-grid.s-padding-left-small.s-padding-right-small.s-span-page.a-spacing-top-small > div > div.a-fixed-left-grid-col.a-col-left > div > div.a-section.a-spacing-base > div.left_nav.browseBox > ul:nth-child(15)"

    def start_requests(self):
        yield scrapy.Request(url=self.elec_url, callback=self.prepare_catagory)

    def prepare_catagory(self, response):
        urls = []
        return urls

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)