
# coding: utf-8

# In[1]:

import pandas


# In[2]:

df = pandas.read_csv('awsLink/workCopy.csv', sep=',')


# In[3]:

#print(df.shape)


# In[4]:

n1 =  df.columns
#print(n1)


# In[5]:

subset = df[['Location', 'Instance Type', 'vCPU', 'Operating System', 'Instance Family', 'Tenancy', 'Memory', 'LeaseContractLength', 'Unit', 'PricePerUnit', 'TermType', 'Currency', 'PurchaseOption']] # subset multiple columns


# In[6]:

#print (subset.head())


# In[7]:

print (subset.shape)


# In[ ]:




# In[8]:

subset['Tenancy'].value_counts()


# In[9]:

# get_ipython().magic('matplotlib inline')


# In[10]:

# subset['Tenancy'].value_counts().plot(kind='bar')


# In[11]:

pick_type = "t2.nano"
print ("PICK is", pick_type)
t2_nano=subset[subset['Instance Type'] == pick_type]


# In[12]:

t2_nano[:6]


# In[13]:

t2_nano.columns


# In[14]:

t2_nano_jr = t2_nano[['Location', 'Operating System', 'LeaseContractLength', 'Unit', 'PricePerUnit', 'Currency','PurchaseOption']]


# In[15]:

#t2_nano_jr[:7]


# In[16]:

t2_nano_1yr=t2_nano_jr[t2_nano_jr['LeaseContractLength'] == "1yr"]


# In[17]:

#t2_nano_1yr[:8]


# In[18]:

t2_nano_1yr_linux=t2_nano_1yr[t2_nano_1yr['Operating System'] == "Linux"]


# In[19]:

#t2_nano_1yr_linux[:10]


# In[20]:

t2_nano_tony=t2_nano_1yr_linux[t2_nano_1yr_linux['Unit'] == "Quantity"]


# In[21]:

#t2_nano_tony


# In[22]:

t2_s = t2_nano_tony.sort_values('Location')


# In[23]:

#t2_s


# In[24]:

t2_a = t2_s[t2_s['PurchaseOption'] == "All Upfront"]


# In[25]:

t2_a


# In[26]:

t2_f = t2_a[['Location', 'PricePerUnit']]


# In[27]:

#t2_f


# In[28]:

t2_cheap = t2_f.sort_values('PricePerUnit')


# In[29]:

print ("TABLE is ",t2_cheap)


# In[30]:

# t2_cheap.plot(kind='bar')


# In[31]:

#t2_cheap.plot(y='PricePerUnit', kind="bar")


# In[32]:

#t2_cheap.plot(x='Location', y='PricePerUnit', kind="bar")


# In[33]:

# t2_cheap.plot(x='Location', y='PricePerUnit', kind="bar", color='orange')


# In[34]:

subset.groupby('Location')['Instance Type'].count()


# In[35]:

# subset.groupby('Location')['Instance Type'].count().plot(kind='bar')


# In[ ]:



