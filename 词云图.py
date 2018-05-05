# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

f=open('test.txt','r',encoding='gb18030')
text=f.readlines()
string='a'
for num in range(0,len(text),4):
    x=text[num]
    a='启航行动'
    s=0
    for t in range(len(x)-4):
        if x[t:t+4]==a :
            s=1
    if s ==0:
        string=string+str(x)
text=string
f.close()

# the font from github: https://github.com/adobe-fonts
font = r'C:\Windows\Fonts\simhei.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(text.lower())
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('show_Chinese.png')
