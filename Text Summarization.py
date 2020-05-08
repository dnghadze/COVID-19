#!/usr/bin/env python
# coding: utf-8

# ## COVID-19 
# 

# In[2]:


from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[3]:


def get_only_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page)
    text = ''.join(map(lambda p: p.text, soup.find_all('c')))
    print(text)
    return soup.title.text,text


# In[4]:


url = 'https://en.wikipedia.org/wiki/Coronavirus_disease_2019'


# In[5]:


text = get_only_text(url)


# In[6]:


len("".join(text))


# In[15]:


#import summarize from gensim
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# In[16]:


text = str(text)


# In[30]:


print(keywords(text, ratio = 0.1))


# In[25]:


a=summarize(text,ratio=0.1)
a


# In[26]:


len(a)


# In[ ]:




