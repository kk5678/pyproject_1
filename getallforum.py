#-*- coding: UTF-8 -*- 
 
from bs4 import BeautifulSoup
import requests
#import lxml
import re

bbsauthor = 'ty_给文明以岁月'
#fpath = r"c:\\python\\想说说我对越南的看法.txt"
url = 'http://bbs.tianya.cn/post-worldlook-1958856-'

infoDict = {}   #初始化存放帖子要获取的全部信息的字典
authorInfo = [] #初始化存放帖子评论的作者的信息的列表
comment = []    #初始化存放帖子评论的信息的列表

fp = open("c:\\temp\\美国有更强大的私有体系，为何有更多人失业经济也在衰退.txt","w+",encoding="utf-8")

for i in range(5):
#获取一个url，通过requests.get()方法，获取页面的信息，这是一个获取url资源的模块
    
    infoDict.clear()
    authorInfo.clear()
    comment.clear()

    urlpage = url + str(i+1) + '.shtml'
    
    r = requests.get(urlpage)
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)

    
    if i == 0:
        Info = soup.find('span',attrs={'style':'font-weight:400;'})
        title = Info.text#//获取帖子的标题
            
        infoDict.update({'论坛话题:  ':title})#//把帖子的标题内容存放到字典中
        print(infoDict)
    
    print("第{0}页: {1}".format(i+1, urlpage))

    author = soup.find_all('div', attrs={'class':'atl-info'})
    #print(author)
    for m in author:
        authorInfo.append(m.text)#//把帖子中的评论的作者的信息存放到列表里
        #print(m.text)

    author = soup.find_all('div', attrs={'class':'bbs-content clearfix', 'class':'bbs-content'})
    for m in author:
        #m.text = m.text.strip()
        #m.text = re.sub('[\r\n\t]', '', m.text)
        comment.append(m.text)#//把帖子的评论的信息存放在列表里
        #print(m.text)

    #print(len(authorInfo))
    #print(len(comment))
    
    for m in range(min(len(authorInfo), len(comment))):
        key = authorInfo[m]+'\n'
        value = comment[m]+'\n'
    
        infoDict[key] = value #//把评论的作者的信息跟评论的内容以键值对的形式存储起来   
        #print(len(infoDict))
        #print(comment[m])

    #把获取到的信息存放在自己指定的位置
    for m in infoDict:
        #result = bbsauthor in str(m)
        #if result == True:
            fp.write(str(m)+'\n')
                
            infoDict[m] = "".join(infoDict[m].split())
            #infoDict[m] = infoDict[m].strip()
            infoDict[m] = infoDict[m].replace("————","/")
            infoDict[m] = infoDict[m].replace("-------","/")

            #deletechar = infoDict[m]
            #infoDict[m] = re.sub('[\r\n\t]', '', deletechar)
            #print(infoDict[m])
            fp.write(str(infoDict[m])+'\n')
        
        #else: continue            

fp.close()