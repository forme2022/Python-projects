#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data.head()


# In[3]:


day_average = data.groupby(["Timestamp"])
day_average.head()


# In[5]:


data["Day"]=data["Timestamp"].dt.month
data.head()


# In[6]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Timestamp"])
day_average.head()


# In[7]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"])
day_average.head()


# In[8]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average.head()


# In[9]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average


# In[10]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
type(day_average)


# In[11]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average.columns


# In[13]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average["Rating"]


# In[14]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average.index


# In[16]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
type(day_average.index)


# In[15]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
list(day_average.index)


# In[18]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
plt.plot(day_average.index, day_average["Rating"])


# In[20]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
plt.figure(figsize=(25,3))
plt.plot(day_average.index, day_average["Rating"])


# In[21]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average.head()


# ### rating average count/day

# In[41]:


data["Day"]=data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()
day_average.head()


# In[42]:


plt.figure(figsize=(25,3))
plt.plot(day_average.index, day_average["Rating"])


# ### rating average count/week

# In[24]:


data


# In[28]:


data["Week"]=data["Timestamp"].dt.week
week_average = data.groupby(["Week"]).count()


# In[31]:


data["Week"]=data["Timestamp"].dt.isocalendar().week
data["Week"]


# In[32]:


data["Week"]=data["Timestamp"].dt.week
data


# In[33]:


data["Week"]=data["Timestamp"].dt.week
data["Week"].max()


# In[34]:


data["Week"]=data["Timestamp"].dt.week
data["Week"].min()


# In[35]:


data["Week"]=data["Timestamp"].dt.isocalendar().week
data["Week"]


# In[36]:


data["Week"]=data["Timestamp"].dt.strftime("%Y %U")
data["Week"]


# In[39]:


data["Week"]=data["Timestamp"].dt.strftime("%Y %U")
week_average=data.groupby(["Week"]).mean()
week_average


# In[43]:


plt.figure(figsize=(25,3))
plt.plot(week_average.index,week_average["Rating"])


# ### average rating by month

# In[49]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average=data.groupby(["Month"]).mean()
month_average


# In[50]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average=data.groupby(["Month"]).mean()
plt.figure(figsize=(25,3))
plt.plot(month_average.index,month_average["Rating"])


# ### average rating by course by month

# In[58]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"]).mean()
month_average_crs


# In[59]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"]).mean()
month_average_crs[-20:]


# In[60]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"]).mean()
month_average_crs[20:]


# In[61]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"]).mean().unstack()
month_average_crs


# In[66]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"]).count().unstack()
month_average_crs.plot(figsize=(25,8))


# In[67]:


month_average_crs


# In[69]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"])["Rating"].count().unstack()
month_average_crs.plot(figsize=(25,8))


# In[70]:


data["Month"]=data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs=data.groupby(["Month","Course Name"])["Rating"].mean().unstack()
month_average_crs.plot(figsize=(25,8))


# ### which day of the week people are happiest?

# In[72]:


data["Weekday"]=data["Timestamp"].dt.strftime("%B")
data


# In[76]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
weekday_average = data.groupby(["Weekday"]).mean()
weekday_average


# In[77]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
weekday_average = data.groupby(["Weekday"]).mean()
plt.plot(weekday_average.index, weekday_average["Rating"])


# In[78]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
weekday_average = data.groupby(["Weekday"]).mean()
weekday_average = weekday_average.sort_values(0)
weekday_average
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[80]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
weekday_average = data.groupby(["Weekday"]).mean()
weekday_average = weekday_average.sort_values("Weekday")
weekday_average.index
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[81]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
data
#weekday_average = data.groupby(["Weekday"]).mean()
#weekday_average = weekday_average.sort_values("Weekday")
#weekday_average.index
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[82]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
weekday_average
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[83]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
weekday_average
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[84]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
plt.plot(weekday_average.index, weekday_average["Rating"])


# In[85]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
weekday_average.index
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[86]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
weekday_average.index.get_level_values(0)
#plt.plot(weekday_average.index, weekday_average["Rating"])


# In[87]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
weekday_average.index.get_level_values(0)
plt.plot(weekday_average.index, weekday_average["Rating"])


# In[88]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")

plt.plot(weekday_average.index.get_level_values(0), weekday_average["Rating"])


# In[89]:


data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")
weekday_average = data.groupby(["Weekday","Daynumber"]).mean()
weekday_average = weekday_average.sort_values("Daynumber")
plt.figure(figsize=(15,3))
plt.plot(weekday_average.index.get_level_values(0), weekday_average["Rating"])


# ### number of ratings by course

# In[90]:


dir(plt)


# In[91]:


help(plt.pie)


# In[92]:


share = data.groupby(["Course Name"]).count()
share


# In[95]:


share = data.groupby(["Course Name"])["Rating"].count()
share


# In[96]:


plt.pie(share)


# In[100]:


plt.pie(share, labels=share.index)


# In[ ]:




