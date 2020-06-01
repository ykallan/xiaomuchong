# 小木虫app爬取
# GET https://mapi.xmcimg.com/bbs/kaoyan.php?emobile=3&page=2 HTTP/1.1

import requests
import re

headers ={
'Host': 'mapi.xmcimg.com',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'cookie': '_discuz_uid=21740431; _discuz_uid=21740431; _discuz_cc=86851267161866986; _discuz_pw=ba624b83edf7446c; _discuz_mobile=1; _emuchos=5b27d5924b69c861|android|208|wifi|0|2|355757969321310|xmc; _discuz_in=1; last_ip=123.245.221.92_21740431; _ga=GA1.2.1488168535.1586180976; _gat=1; Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569=1586180994; Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569=1586180994; Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569=1586180995; Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569=1586180995; _discuz_mobile=1',
'x_zyj_user_agent': 'zyjapp/208(uid/21740431 os/android net/wifi)',
'x_zyj_auth': 'Accept-Encoding: gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'X-Requested-With': 'com.zhuanyejun.club',
}
# Content-Encoding: gzip
req_url = 'https://mapi.xmcimg.com/bbs/kaoyan.php?emobile=3&page=2'
for i in range(20):
    print(i+1)
    req_url = 'https://mapi.xmcimg.com/bbs/kaoyan.php?emobile=3&page={}'.format(i+1)
    resp = requests.get(url=req_url,headers=headers,verify=False)
# print(resp.text)
    next_ids = re.findall(r'tid%3D(\d+)%26',resp.text)
    print(next_ids)

req_url2 = 'https://mapi.xmcimg.com/bbs/viewthread.php?tid=14176781&emobile=3&kyusername=&f=&w='
resp2 = requests.get(url=req_url2,headers=headers,verify=False)
# print(resp2.text)