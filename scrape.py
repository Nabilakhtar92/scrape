#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'


# In[3]:


page = requests.get(url)
page.content


# In[10]:


soup=BeautifulSoup(page.content ,'html.parser')
soup


# In[15]:


heading = soup.findAll(attrs = {'class':'tdb-title-text'})


# In[18]:


heading[0].text


# In[44]:


article = soup.findAll(attrs = {'class':'tdb-block-inner td-fix-index'})


# In[49]:


article




# In[56]:


article


# In[ ]:




