# NUAA Data Analysis of Social Practice in Summer Vacation
#### 运行环境  
Python3.6

#### 功能说明
爬去南航行知平台（http://up.nuaa.edu.cn/）  上2018年南航大学生暑假社会实践的信息并对其经行分析。  

#### 环境
运行本程序需要如下环境:  
requests  
>pip install requests

pyecharts  

>pip install pyecharts

对于Python中生成词云，需要安装WordCloud，他的安装不像上面的简单，如果只是通过pip安装的话会出现很多莫名其妙的错误。
>下载相应版本的whl文件，从http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud  
进入相应文件件  
在管理员环境下运行python -m pip install <filename>    

其余的所需环境不再一一赘述，请缺少的自行谷歌百度搜索安装。

#### 代码流程
1.先获取项目网页的html，然后通过bs4（BeautifulSoup4）对其分析，提取所需的内容。  
2.因为项目地址没有统一格式，无法提取准确的地址，所以将项目地址逐个上传腾讯地图服务器，获得准确的地址信息。  
3.对获得的城市信息进行分析和筛选，获得相应的次数。  
4.绘制图表。  
5.对项目名称进行词频分析构建词云。
