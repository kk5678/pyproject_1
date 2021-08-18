#from fake_useragent import UserAgent
import requests
import json
import pandas as pd

#ua=UserAgent()
#请求的网址
url="https://www.9kd.com/api/kd-content/contents/list/pc"
#请求头
headers= {"Accept": 'application/json, text/plain, */*', "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive", "Content-Length": "69", "Content-Type": "application/json;charset=UTF-8", "Cookie": "Hm_lvt_f23477377aa0bd1dc93743229bb437b7=1627176380; Hm_lvt_49b9ec0752fc32fa94fb88844e9bc707=1627176380; Hm_lpvt_f23477377aa0bd1dc93743229bb437b7=1627187929; Hm_lpvt_49b9ec0752fc32fa94fb88844e9bc707=1627187929", "Host": "www.9kd.com", "Origin": "https://www.9kd.com", "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"92\"", "sec-ch-ua-mobile": "?0", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

data={
    "firstId": 0,
    "lastId": 0,
    "limit": 50,
    "page": 1,
    "product": "2",
    "tagId": 90
}
#请求网址
response=requests.post(url=url,headers=headers,data=json.dumps(data))

#响应体内容
#print(json.dumps(json.loads(response.text),sort_keys=True, indent=4,ensure_ascii=False))
#print(json.loads(response.text))
#响应状态信息
print(response.status_code)
#响应头信息
print(response.headers)

df=pd.DataFrame(json.loads(response.text))
print(df['data']['list'])
df1=pd.DataFrame(df['data']['list'])
print(df1)
df1.to_excel("凯迪新闻爬虫输出-海南资讯.xlsx")
