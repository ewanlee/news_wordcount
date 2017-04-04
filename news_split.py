
# coding: utf-8

# In[27]:

import os
import io
from bosonnlp import BosonNLP


# In[3]:

# Get news file path
news_dir = '/home/ewan/Documents/news_spider/news_20/'
file_list = os.listdir(news_dir)


# In[6]:

print file_list[0]


# In[24]:

# Get the news dict
news = {}
for index, file in enumerate(file_list):
    with io.open(news_dir + file, 'r') as f:
        news[index] = file.decode('utf-8') + '\n' + f.read()


# In[19]:

file_list[0]


# In[20]:

file_list[0].decode('utf-8')


# In[26]:

print news[0]


# In[28]:

nlp = BosonNLP('FuHSE7Vf.13924.jadflTdrQLWx')
splitted_news = {}

SIZE = len(news)

for key, value in news.items():
    result = nlp.tag([value])
    words = ''
    for index, word in enumerate(result[0]['word']):
            words += word + ' '
    splitted_news[key] = words


# In[34]:

for index, content in splitted_news.items():
    with io.open(str(index), 'w') as f:
        f.write(content)

