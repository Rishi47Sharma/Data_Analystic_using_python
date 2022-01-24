#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[50]:


df=pd.read_csv("E:/NPTEL_DATA_ANALYSTICS/gapminder-FiveYearData.csv")


# In[48]:


df


# In[34]:


df.shape


# In[36]:


df.columns


# In[42]:


df.head(10)


# In[45]:


df.tail(n=1
)


# In[51]:


df.info()


# In[62]:


variable=df['country']


# In[64]:


variable.head()


# In[81]:


loc=df.loc[:,['country','pop']]
    


# In[82]:


print(loc.head())


# In[89]:


var=df.groupby(['year','continent'])[['lifeExp','pop']].mean()


# In[90]:


print(var)


# In[91]:


var.plot()


# In[ ]:




