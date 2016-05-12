# coding:utf-8
import random
import base64
from settings import PROXIES


class RandomUserAgent(object):
    """choose a user agent from PROXIES in setting"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# class ProxyMiddleware(object):
#
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXIES)
#         if proxy['user_pass'] is not None:
#             request.meta['proxy'] = 'http://%s' % proxy['ip_port']
#             encoded_user_pass = base64.encodestring(proxy['user_pass'])
#             request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#             print 'ProxyMiddlerware have pass' + proxy['ip_port']
#         else:
#             print 'ProxyMiddleware no pass' + proxy['ip_port']
#             request.meta['proxy'] = 'http://%s' % proxy['ip_port']
