import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
from PIL import Image

text=open('C:\\Users\ADmin\Documents\wordcloud.txt','r').read()

wc=WordCloud(background_color='white')
wc.generate(text)

plt.imshow(wc,interpolation='bilinear')
plt.axis=('off')
plt.show()
