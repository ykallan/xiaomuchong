# -*- coding: utf-8 -*-
import scrapy
import re
from xiaomuchong.items import XiaomuchongItem


class XmcSpider(scrapy.Spider):
    name = 'xmc'
    allowed_domains = ['xmcimg.com']
    start_urls = ['http://xmc.com/']
    def start_requests(self):
        for i in range(10000):
            # print(i + 1)
            req_url = 'https://mapi.xmcimg.com/bbs/kaoyan.php?emobile=3&page={}'.format(i + 1)
            # resp = requests.get(url=req_url, headers=headers, verify=False)
            yield scrapy.Request(url=req_url,callback=self.parse)

    def parse(self, response):
        # print(response.text)
        # '<a href="http://muchong.com/t-14178593-1-emobile-1" >'
        next_ids = re.findall(r'com/t-(\d+)-1-', response.text)
        # print(next_ids)
        req_url2 = 'https://mapi.xmcimg.com/bbs/viewthread.php?tid={}&emobile=3&kyusername=&f=&w='
        for k in next_ids:
            yield scrapy.Request(url=req_url2.format(k), callback=self.parse_detial)

    def parse_detial(self, response):
        item = XiaomuchongItem()
        # print(response.text)
        title = response.xpath('//h1/text()').extract_first()
        # print(title)
        xuexiao = response.xpath('//div[@class="detail"][1]/dd[1]/text()').extract_first()
        # print(xuexiao[3:])
        zhuanye = response.xpath('//div[@class="detail"][1]/dd[2]//text()').extract_first()
        # zhuanye_span = response.xpath('//div[@class="detail"][1]/dd[2]//span/text()').extract_first()
        nianji = response.xpath('//div[@class="detail"][1]/dd[3]/text()').extract_first()
        # print(nianji[3:])
        zhaoshengzhuangtai = response.xpath('//div[@class="detail"][1]/dd[4]/text()').extract_first()
        zhaoshengrenshu = response.xpath('//div[@class="detail"][1]/dd[5]/text()').extract_first()
        lianxifangshi = response.xpath('//div[@class="detail"][1]/dd[6]/text()').extract_first()
        # print(xuexiao,zhuanye,nianji,zhaoshengzhuangtai,zhaoshengrenshu,lianxifangshi)
        xiangqings = response.xpath('//div[@class="inner"]/div[@class="pbd"][1]/text()').extract()
        # print(xiangqings)
        xiangqing2 = ''.join(i.replace('\n', '').replace('\r','').replace('\xa0','') for i in xiangqings)
        xiangqing = xiangqing2.split('总分:')[0]
        # print(xiangqing)
        item['title'] = title[6:]
        item['xuexiao'] = xuexiao[3:]
        item['zhuanye'] = zhuanye[3:].strip()
        item['nianji'] = nianji[3:]
        item['zhaoshengzhuangtai'] = zhaoshengzhuangtai[5:].strip()
        item['zhaoshengrenshu'] = zhaoshengrenshu[5:].strip()
        if '-' in zhaoshengrenshu[5:].strip():
            item['zhaoshengrenshu'] = '未知'
        if len(zhaoshengrenshu[5:].strip()) == 0:
            item['zhaoshengrenshu'] = '未知'
        item['lianxifangshi'] = lianxifangshi[5:].strip()
        if len(lianxifangshi[5:].strip())==0:
            item['lianxifangshi'] = '未知'
        item['xiangqing'] = xiangqing
        '''
        print('标题：',item['title'])
        print('学校：',item['xuexiao'])
        print('专业：',item['zhuanye'])
        print('年级：',item['nianji'])
        print('招生状态：',item['zhaoshengzhuangtai'])
        print('招生人数',item['zhaoshengrenshu'])
        print('联系方式',item['lianxifangshi'])
        print('详情：',xiangqing)
        '''

        yield item



