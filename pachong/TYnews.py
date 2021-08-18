import requests
from lxml import etree
import re
import pandas as pd
resultlist=[]
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
    }
for i in range(2):
    url = 'http://news.hainan.net/hainan/list_{0}.shtml'.format(i+1)
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="cms_Location_12"]/div[1]/div[1]/ul/li/h3/a/@href')

    for li in li_list:
        response=requests.get(url=li,headers=headers)
        content=response.content.decode("utf8")
        tree = etree.HTML(content)
        arc_title = tree.xpath('//*[@id="subject"]/text()')[0]
        try:
            arc_time=tree.xpath('//*[@id="cms_fragment_235_bd"]/div/div[2]/div/text()')[-2]
            arc_time=re.sub(r'[\r\n]*','',arc_time).lstrip()
        except:
            try:
                arc_time = tree.xpath('//*[@id="cms_control_365"]/div/div[2]/div/ul/li[3]/text()')[0]
                arc_time = re.sub(r'[\r\n]*','',arc_time).lstrip()
            except:
                continue

        result_li={
            'arc_title':arc_title,
            'arc_time':arc_time,
            'url': li,
        }
        resultlist.append(result_li)
    print("第{0}轮爬虫完成".format(i+1))
df=pd.DataFrame(resultlist)
df.to_excel("海南在线爬虫输出-海南资讯.xlsx")
