# coding:utf-8
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from douban_reviews.items import DoubanReviewsItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DoubanSpider(Spider):
    """douban reviews spider"""
    # name of spider
    name = "douban"
    # allowed domain
    allowed_domains = {"movie.douban.com"}
    # start url
    start_urls = ["https://movie.douban.com/subject/10831445/reviews"]

    # start crawler
    def start_requests(self):
        yield self.make_requests_from_url(self.start_urls[0])

    def parse(self, response):
        """response handler of main url"""
        selector = Selector(response)
        # extract url of full review
        full_review_url = selector.xpath('//div[@class="review-hd"]/h3/a[2]/@href').extract()
        for url in full_review_url:
            yield Request(url, callback=self.full_review_handler)

        # extract url of next page
        next_page = selector.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract()
        next_page_url = str(self.start_urls[0]).strip() + "/" + str(next_page[0]).strip()
        yield Request(next_page_url, callback=self.parse)

    def full_review_handler(self, response):
        """extract full review"""
        # replace <br>
        response = response.replace(body=response.body.replace('<br>', ''))
        selector = Selector(response)
        douban_item = DoubanReviewsItem()

        reviewer = selector.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/p/a[2]/span/text()').extract()
        douban_item['reviewer'] = reviewer

        reviewer_link = selector.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/p/a[2]/@href').extract()
        douban_item['reviewer_link'] = [r.decode('utf-8') for r in reviewer_link]

        rating_title = selector.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/p/span[1]/@title').extract()
        douban_item['rating_title'] = [r.decode('utf-8') for r in rating_title]

        rating = selector.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/p/span[2]/text()').extract()
        douban_item['rating'] = [r.decode('utf-8') for r in rating]

        time = selector.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/p/span[3]/text()').extract()
        douban_item['time'] = [t.decode('utf-8') for t in time]

        douban_item['review_link'] = response.url

        title = selector.xpath('//*[@id="content"]/h1/span/text()').extract()
        douban_item['title'] = [t.decode('utf-8') for t in title]

        review_full = selector.xpath('//*[@id="link-report"]/div[1]/text()').extract()
        review_full = [r.decode('utf-8') for r in review_full]

        if len(review_full[0]) > 200:
            review_short = (review_full[0])[0:200]
        else:
            review_short = review_full
        douban_item['review_short'] = review_short
        douban_item['review_full'] = review_full

        review_useful = selector.xpath('//div[@class="main-panel-useful"]/span[1]/em/text()').extract()
        douban_item['review_useful'] = [r.decode('utf-8') for r in review_useful]

        review_unuseful = selector.xpath('//div[@class="main-panel-useful"]/span[2]/em/text()').extract()
        douban_item['review_unuseful'] = [u.decode('utf-8') for u in review_unuseful]
        yield douban_item





