

from os import path
from wordcloud import WordCloud
import jieba


# 读取整个文本
file=open('1.txt')

text =file.read()
text=''.join(jieba.cut(text))

# 生成一个词云图像
wordcloud = WordCloud(font_path="C:\Windows\Fonts\simhei.ttf").generate(text)

# matplotlib的方式展示生成的词云图像
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#max_font_size设定生成词云中的文字最大大小
#width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是他对中文支持不好
wordcloud = WordCloud(font_path="C:\Windows\Fonts\simhei.ttf" , max_font_size=66).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# pil方式展示生成的词云图像（如果你没有matplotlib）
#image = wordcloud.to_image()
#image.show()
