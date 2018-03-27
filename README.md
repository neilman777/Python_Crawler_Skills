# Python_Crawler_Skills
There are 3 common skills I ususally use to crawl a website.
+ use **requests**
+ use **BeautifulSoup**
+ use **Regular Expression**

## 1. requests
For any website I want to crawl, I **always** use **requests** to start because I can easily get all html content by call requests method.
like this:
``` python
# if url of the website I want to crawl is : https://buy.yungching.com.tw/region/
import requests
url = 'https://buy.yungching.com.tw/region/'
headers1={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': 103,
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': '__ltm_https_flag=true; __ltmwga=utmcsr=google|utmcmd=organic; userid=b5bb6508-56cb-41cb-be12-0333982f6b61; _ga=GA1.3.1572858197.1522119239; _gid=GA1.3.551830587.1522119239; __asc=deaf4d2f1626560663e3803ceb0; __auc=deaf4d2f1626560663e3803ceb0; TRID_G=4050a687-062a-4230-af50-523028904ba6; yawbewkcehc=0; ez2o_UNID=1522119243851851; _ga=GA1.4.1572858197.1522119239; _gid=GA1.4.551830587.1522119239; _pk_ref.5.f7c6=%5B%22%22%2C%22%22%2C1522119244%2C%22https%3A%2F%2Fwww.yungching.com.tw%2F%22%5D; _pk_ses.5.f7c6=*; _last_search_data=%7B%22searchFor%22%3A%22all%22%2C%22mainType%22%3A%22region%22%2C%22addr%22%3A%5B%5B%22%E5%8F%B0%E5%8C%97%E5%B8%82%22%5D%2C%5B%22%22%5D%5D%2C%22mrt%22%3A%5B%5D%2C%22isMap%22%3Afalse%2C%22price%22%3A%5B%22%22%2C%22%22%5D%2C%22pyeong%22%3A%5B%22%22%2C%22%22%5D%2C%22keywords%22%3A%5B%22%22%5D%2C%22filterBy%22%3A%5B%22%22%5D%2C%22sortBy%22%3A%5B%22undefined%22%5D%2C%22advConditions%22%3A%7B%22car%22%3A%5B%5D%2C%22houseType%22%3A%5B%5D%2C%22accessible%22%3A%5B%5D%2C%22houseAge%22%3A%5B%5D%2C%22directions%22%3A%5B%5D%2C%22floors%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22rooms%22%3A%7B%22sp%22%3A%5B%22false%22%5D%2C%22val%22%3A%5B%5D%7D%2C%22sp%22%3A%5B%5D%7D%2C%22od%22%3A%22%22%2C%22pyeongType%22%3A0%2C%22coords%22%3A%22%22%2C%22searchBland%22%3A%22%E5%85%A8%E9%83%A8%E4%BB%B2%E4%BB%8B%22%2C%22originalDomain%22%3A%22%22%7D; _pk_id.5.f7c6=632dc12a53b6bd62.1522119244.1.1522120030.1522119244.; _uetsid=_uet119f5fbe; _gat_UA-35108030-1=1',
    'Host': 'buy.yungching.com.tw',
    'Origin': 'https://buy.yungching.com.tw',
    'Pragma': 'no-cache',
    'Referer': 'https://buy.yungching.com.tw/region/%E5%8F%B0%E5%8C%97%E5%B8%82-_c/?pg=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

response = requests(url, headers=headers1)
response.text


```

response.text is a string of html of the url.


#### response encode
If we don't specified what encode type we want for the response, requests will **auto-detect** the property encode type. For safety, we can specified the encode type by **response.encoding = "code_name"**. like this:
``` python
response = requests(url, headers=headers1)
response.encoding = 'utf-8'
```

#### common-use method of Module requests
+   
+   



# 2. BeautifulSoup4
**After we get the response of website**, then we can start to dig data we want from the **html response**.

Using BeautifulSoup4 module is **one of the methods** to access data we want.

To use BeautifulSoup4, we need to install **bs4** module first by use terminal.
``` bash 
pip install BeautifulSoup4
```
Then import class **BeautifulSoup** of **bs4**.
``` python
from bs4 import BeautifulSoup
```


