# -*- coding: utf-8 -*-
#coding=utf-8


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
import matplotlib.pyplot as plt
from scipy.misc import imread



text = open('wordclodtext.txt','r',encoding='utf8').read()
print(text)
bg_pic = imread('test.png')

wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)
image_colors = ImageColorGenerator(bg_pic)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('gencloud.jpg')
