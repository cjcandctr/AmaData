import scrapy


class QuotesSpider(scrapy.Spider):
    name = "techSpy"
    FILE_SIZE = 10
    file_vol = 0

    start_url_elec = "https://www.amazon.com/s/ref=lp_1292110011_ex_n_1?rh=n%3A172282&bbn=172282&ie=UTF8&qid=1519961320"
    test_url = 'https://www.amazon.com/s/ref=lp_11548951011_nr_n_0?fst=as%3Aoff&rh=n%3A172282%2Cn%3A%21493964%2Cn%3A541966%2Cn%3A172456%2Cn%3A11548951011%2Cn%3A3015405011&bbn=11548951011&ie=UTF8&qid=1520574780&rnid=11548951011'
    catagory_l3_url =[]
    l3_pth = '//*[@id="a-page"]/div[4]/div/div[2]/div/div[2]/div[2]/ul['    
    
    #scrapy %windir%\system32\cmd.exe "/K" "C:\Program Files\Anaconda3\Scripts\activate.bat" "C:\Program Files\Anaconda3"
    #meta = { 'dont_redirect': True, 'handle_httpstatus_list': [301] }
    def start_requests(self):
        #yield scrapy.Request(url=self.start_url_elec, callback=self.parse_l3_catagory)
        yield scrapy.Request(url=self.test_url, callback=self.test_request)

    def test_request(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)

    def parse_l3_catagory(self, response):
        for i in range(4,14):
            l3_xpath = self.l3_pth + str(i) + ']'
            for li in response.xpath(l3_xpath):
                self.catagory_l3_url.append(response.urljoin(li.css("a::attr(href)").extrac_first()))
        for turl in self.catagory_l3_url:
            yield scrapy.Request(url=turl, callback= self.parse_sub_item)

    def parse_sub_item(self, response):
        #for sub in response.xpath()

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)