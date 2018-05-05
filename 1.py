import requests
from bs4 import BeautifulSoup
from pyecharts import Geo
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt

#获得返回页面，并对其进行进本排版
def html(url):
    html_url=requests.get(url)
    soup=BeautifulSoup(html_url.text,'lxml')
    #print (soup)
    return soup

#通过BS4将需要的内容提取出来存到本地中
def aaa(soup):
    b=soup.find_all('h2',class_="media-heading")
    for name in b :
        print(name.get_text())
        if name!=' ':
            f = open('test.txt', 'a',encoding='gb18030')
            f.write(name.get_text())
            f.write('\n')
            f.close()
    a=soup.find_all('div',class_="time")
    #print(a)
    for name in a[:3] :
        print(name.get_text())
        if name!=' ':
            f = open('test.txt', 'a',encoding='gb18030')
            f.write(name.get_text())
            f.write('\n')
            f.close()

#通过腾讯地图的API，获得项目地址所在的城市
def location():
    f = open('test.txt', 'r',encoding='gb18030')
    c=f.readlines()
    location_list=[]
    for num in range(3,len(c),4):
        c[num]=c[num][6:]
        a=str(c[num])
        a=requests.get('http://apis.map.qq.com/ws/geocoder/v1/?address=%s&key=5KJBZ-QX6K3-ELY3Z-Y2MYG-NO4O7-SWF4E' % a )
        if (a.json()['status'])==0:
            print(a.json()['result']['address_components']['province'])
            if a.json()['result']['address_components']['province'][-1]=='市':
                location_list.append(a.json()['result']['address_components']['province'][:-1])
            else:
                location_list.append(a.json()['result']['address_components']['province'])
    f.close()
    print(location_list)
    trush_list=[]
    trush_list2=[]
    trush_list3=[]
    trush_list4=[]
    for num in range(len(location_list)):
        if location_list[num] == '台南':
            trush_list.append(num)
        if location_list[num] == '香港特别行政区':
            trush_list2.append(num)
        if location_list[num] == '宣城':
            trush_list3.append(num)
        if location_list[num] == '固原':
            trush_list4.append(num)
    print(trush_list)
    t=0
    for x in trush_list:
        location_list.pop(x-t)
        t=t+1
    d=0
    for x in trush_list2:
        location_list.pop(x-d)
        d=d+1
    e=0
    for x in trush_list3:
        location_list.pop(x-e)
        e=e+1
    f=0
    for x in trush_list4:
        location_list.pop(x-f)
        f=f+1
    print(location_list)
    f = open('tes2t.txt', 'a',encoding='gb18030')
    for x in location_list:
        f.write(x)
        f.write('\n')
    f.close()
    return location_list

#计算相应城市出现的次数
def calu(location_list):
    calu_list=[]
    for flag in location_list:
        flag_num=0
        for flag2 in location_list:
            if flag2==flag:
                flag_num=flag_num+1
        a=(flag,flag_num)
        calu_list.append(a)
    calu_list=list(set(calu_list))
    print(calu_list)
    return calu_list

#将数据表示在地图上
def Pic(data):
    geo = Geo("南航暑假社会实践目的地示意图(部分)", "Data from h1997l1997", title_color="#fff",
              title_pos="center", width=1200,
              height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value,visual_range=[0, 10], visual_text_color="#fff",
            symbol_size=15, is_visualmap=True)
    geo.render()

if __name__ == '__main__':
    for number in range(4071,4663):
        number=str(number)
        url='http://up.nuaa.edu.cn/index.php?m=&c=project&a=show&id='+number
        print(url)
        soup=html(url)
        aaa(soup)
    location_list=location()
    location_list=f.readlines()
    data=calu(location_list)
    Pic(data)
