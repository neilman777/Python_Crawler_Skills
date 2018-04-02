# coding=utf-8

import json
import re
import requests
from bs4 import BeautifulSoup
import sys

dir_path = sys.argv[1]

#url = 'https://buy.yungching.com.tw/region/%E5%8F%B0%E5%8C%97%E5%B8%82-_c/'

header_s={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'_last_search_data=%7B%22searchFor%22%3A%22all%22%2C%22mainType%22%3A%22region%22%2C%22addr%22%3A%5B%5B%22%E5%8F%B0%E5%8C%97%E5%B8%82%22%5D%2C%5B%22%22%5D%5D%2C%22mrt%22%3A%5B%5D%2C%22isMap%22%3Afalse%2C%22price%22%3A%5B%22%22%2C%22%22%5D%2C%22pyeong%22%3A%5B%22%22%2C%22%22%5D%2C%22keywords%22%3A%5B%22%22%5D%2C%22filterBy%22%3A%5B%22%22%5D%2C%22sortBy%22%3A%5B%22undefined%22%5D%2C%22advConditions%22%3A%7B%22car%22%3A%5B%5D%2C%22houseType%22%3A%5B%5D%2C%22accessible%22%3A%5B%5D%2C%22houseAge%22%3A%5B%5D%2C%22directions%22%3A%5B%5D%2C%22floors%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22rooms%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22sp%22%3A%5B%5D%7D%2C%22od%22%3A%22%22%2C%22pyeongType%22%3A0%2C%22coords%22%3A%22%22%2C%22searchBland%22%3A%22%E5%85%A8%E9%83%A8%E4%BB%B2%E4%BB%8B%22%2C%22originalDomain%22%3A%22%22%7D; userid=4ab02f33-f90f-4578-bde1-e0799e65d646; TRID_G=e0bcf196-3909-493e-acd2-795fb5d4b925; ez2o_UNID=1522215564489490; __ltmwga=utmcsr=(direct)|utmcmd=(none); WMX_Channel=,1,; _last_search_data=%7B%22searchFor%22%3A%22all%22%2C%22mainType%22%3A%22region%22%2C%22addr%22%3A%5B%5B%22%E5%8F%B0%E5%8C%97%E5%B8%82%22%5D%2C%5B%22%22%5D%5D%2C%22mrt%22%3A%5B%5D%2C%22isMap%22%3Afalse%2C%22price%22%3A%5B%22%22%2C%22%22%5D%2C%22pyeong%22%3A%5B%22%22%2C%22%22%5D%2C%22keywords%22%3A%5B%22%22%5D%2C%22filterBy%22%3A%5B%22%22%5D%2C%22sortBy%22%3A%5B%22undefined%22%5D%2C%22advConditions%22%3A%7B%22car%22%3A%5B%5D%2C%22houseType%22%3A%5B%5D%2C%22accessible%22%3A%5B%5D%2C%22houseAge%22%3A%5B%5D%2C%22directions%22%3A%5B%5D%2C%22floors%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22rooms%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22sp%22%3A%5B%5D%7D%2C%22od%22%3A%22%22%2C%22pyeongType%22%3A0%2C%22coords%22%3A%22%22%2C%22searchBland%22%3A%22%E5%85%A8%E9%83%A8%E4%BB%B2%E4%BB%8B%22%2C%22originalDomain%22%3A%22%22%7D; userid=4ab02f33-f90f-4578-bde1-e0799e65d646; _gat_UA-35108030-1=1; _dc_gtm_UA-35108030-1=1; yawbewkcehc=0; __asc=582560d51626b1e3bd135ad7d44; __auc=5983cf801626561cf77f6c77d0b; __ltm_https_flag=true; _pk_id.5.f7c6=0225278645f347ab.1522119332.2.1522216079.1522215567.; _pk_ses.5.f7c6=*; _uetsid=_uetafb7b681; _ga=GA1.4.1967887631.1522119332; _gid=GA1.4.1424818617.1522215566',
    'Host':'buy.yungching.com.tw',
    'Pragma':'no-cache',
    'Referer':'https://buy.yungching.com.tw/region/%E5%8F%B0%E5%8C%97%E5%B8%82-_c/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

###
def get_items_from_page(url, header_s, pg_num):
    real_url = url+'?pg='+str(pg_num)
    yungching_items = {}
    items_info = []
    try:
        res = requests.get(real_url, headers=header_s)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, "html5lib")
        items_list = soup.select('.l-item-list .m-list-item')
        total_items_num = len(items_list)
        print("total items num = %s"%total_items_num)
        for num in range(total_items_num):
            one_item_info = {}
            one_item_info['item-description'] = re.sub(' +', ' ', items_list[num].select('.item-info .item-description')[0].text.replace('\xa0', '').replace('\n', ' ').replace('\u3000', ''))
            one_item_info['item-info-detail'] = re.sub(' +', ' ', items_list[num].select('.item-info .item-info-detail')[0].text.replace('\n', ' ').strip())
            item_tags_num = len(items_list[num].select('.item-info .item-tags span'))
            print('tags num = %s'%item_tags_num)
            one_item_info['item-tags'] = []
            for tag_num in range(item_tags_num):
                one_item_info['item-tags'].append(items_list[num].select('.item-info .item-tags span')[tag_num].text)
            one_item_info['item-price'] = items_list[num].select('.item-price .price .price-num')[0].text
            one_item_info['title'] = items_list[num].select('.item-info a')[0]['title'].split(' ',1)[0]
            one_item_info['address'] = items_list[num].select('.item-info a')[0]['title'].split(' ',1)[1]
            one_item_info['detail-href'] = items_list[num].select('.item-info a')[0]['href']
            items_info.append(one_item_info)
            print('%s append succeed'%str(num))
        yungching_items['items_info'] = items_info
        with open(dir_path+'/yungching_items_pg'+str(pg_num)+'.json', 'w', encoding='utf-8') as outfile:
            json.dump(yungching_items, outfile, ensure_ascii=False)
        print('[INFO]Done crawl page %s'%pg_num)
        #return yungching_items
    except:
        print("wrong url")
    
    
    
def get_total_pg_num(url, header_s):
        res = requests.get(url, headers=header_s)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, "html5lib")
        total_pg_num = int(re.findall( 'pg=(\d{,5})', soup.select('.m-pagination-bd li a[ga_label="buy_page_last"]')[0]['href'])[0])
        return total_pg_num

def yungching_crawler(url, header_s):
    total_pg_num = get_total_pg_num(url, header_s)
    print('total pages num = %s'%total_pg_num)
    for pg_num in range(1, total_pg_num+1):
        get_items_from_page(url, header_s, pg_num)
		
url = 'https://buy.yungching.com.tw/region/%E5%8F%B0%E5%8C%97%E5%B8%82-_c/'
yungching_crawler(url, header_s)