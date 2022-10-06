#!/usr/bin/env python
# coding: utf-8

# ## 1.overview of dataframe

# In[61]:


import pandas
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
from datetime import datetime
from pytz import utc


# In[7]:


data


# In[8]:


data.head()


# In[10]:


data.shape


# In[11]:


data.columns


# In[12]:


data.hist("Rating")


# ## 2.select data from the dataframe

# ### select a column

# In[13]:


data["Rating"]


# ### select multiple columns

# In[16]:


data[["Course Name","Rating"]]


# In[17]:


type(data[["Course Name","Rating"]])


# In[18]:


type(data["Rating"])


# ### selecting a row

# In[21]:


data.iloc[3]


# In[20]:


type(data.iloc[3])


# ### selecting mutiple rows

# In[22]:


data.iloc[1:3]


# ### selecting a section

# In[25]:


data[["Course Name","Rating"]]


# In[26]:


data[["Course Name","Rating"]].iloc[1:3]


# ### selecting a cell

# In[27]:


data["Timestamp"].iloc


# In[28]:


data["Timestamp"].iloc


# In[29]:


data["Timestamp"].iloc[2]


# In[30]:


type(data["Timestamp"].iloc[2])


# In[31]:


type(data["Rating"].iloc[2])


# In[33]:


data["Rating"].iloc[2]


# In[34]:


data.at[2,"Rating"]


# ## 3.filtering data based on conditions

# ### one condition

# In[36]:


data[data["Rating"]> 4] 


# In[37]:


len(data[data["Rating"]> 4] )


# In[38]:


data[data["Rating"]> 4].count


# In[39]:


data[data["Rating"]> 4] ["Rating"]


# In[ ]:





# In[39]:


data[data["Rating"]> 4] ["Rating"]


# In[ ]:





# In[40]:


d2= data[data["Rating"]> 4]
d2


# In[ ]:





# In[42]:


d2= data[data["Rating"]> 4]
d2["Rating"].mean()


# ### multiple conditons

# In[ ]:


data[() & ()]


# In[ ]:





# In[49]:


data[(data["Rating"]> 4) & (data["Course Name"] == "The Python Mega Course: Build 10 Real World Applications")]


# In[ ]:





# In[51]:


data[(data["Rating"]> 4) & (data["Course Name"] == "The Python Mega Course: Build 10 Real World Applications")]["Rating"].mean()


# ## 4. time-based filtering

# In[55]:


data[(data["Timestamp"] >= datetime(2020,7,1)) & (data["Timestamp"] <= datetime(2020,12,31))]


# In[ ]:





# In[57]:


data[(data["Timestamp"] >= datetime(2020,7,1)) & (data["Timestamp"] <= datetime(2020,12,31))]


# In[59]:


data["Timestamp"]


# In[ ]:





# In[62]:


data[(data["Timestamp"] >= datetime(2020,7,1, tzinfo=utc)) & (data["Timestamp"] <= datetime(2020,12,31, tzinfo=utc))]


# ## 5.from data to information

# ### average rating

# In[63]:


data["Rating"].mean()


# ### average Rating for a particular course

# In[64]:


data[data["Course Name"] == "The Python Mega Course: Build 10 Real World Applications"]["Rating"].mean()


# ### average rating for a particular period

# In[67]:


data[(data["Timestamp"] >= datetime(2020,1,1, tzinfo=utc)) &
     (data["Timestamp"] <= datetime(2020,12,31, tzinfo=utc))]["Rating"].mean()


# ### average rating for a particular period for a particular course

# In[69]:


data[(data["Timestamp"] >= datetime(2020,1,1, tzinfo=utc)) &
     (data["Timestamp"] <= datetime(2020,12,31, tzinfo=utc)) &
     (data["Course Name"] == "The Python Mega Course: Build 10 Real World Applications")
    ]["Rating"].mean()


# ### average of uncommented ratings

# In[74]:


data[data["Comment"].isnull()]["Rating"].mean()


# ### average of commented ratings

# In[75]:


data[data["Comment"].notnull()]["Rating"].mean()


# ### number of uncommented ratings

# In[78]:


data[data["Comment"].isnull()]["Rating"].count()


# ### number of commented ratings

# In[79]:


data[data["Comment"].notnull()]["Rating"].count()


# ### number of comments containing a certain word

# In[80]:


data[data["Comment"].str.contains("accent")]


# In[ ]:





# In[82]:


data[data["Comment"].str.contains("accent", na=False)]["Rating"].count()


# ### average of  commented ratings with  "accent" in comment

# In[83]:


data[data["Comment"].str.contains("accent", na=False)]["Rating"].mean()


# In[ ]:




