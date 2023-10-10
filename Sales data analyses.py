#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sales data analysis project
            


# In[2]:


import pandas as pd
import os


# In[3]:


#merging all 12 monthly files to get a yearly data


# In[4]:


all = [file for file in os.listdir("C:\Data analysis project\Sales_Data")]
yearly_data = pd.DataFrame()

for file in all:
    df = pd.read_csv("C:\Data analysis project\Sales_Data/"+file)
    yearly_data = pd.concat([yearly_data,df])

yearly_data.to_csv("all_data.csv", index=False)


# In[5]:


all_data = pd.read_csv('all_data.csv')
all_data.head()


# In[6]:


#cleaning data


# In[7]:


nan_data = all_data[all_data.isna().any(axis=1)]
nan_data.head(10)

all_data = all_data.dropna(how = 'all')


# In[8]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head()


# Converting columns to correct datatypes

# In[9]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

all_data.head()


# #additinal coumns

# Adding Month column

# In[10]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')



# Adding City Column

# In[11]:


def find_city(address):
    return address.split(',')[1]

def find_state(state):
    return state.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: find_city(x)+ ' (' +find_state(x) + ')')
all_data.head()


# Adding column for Total amount for each order

# In[12]:


all_data['Total_amt_per_order'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# Best performing month and amount earned during it

# In[13]:


results = all_data.groupby('Month').sum()
results.head(20)


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


months = range(1,13)

plt.bar(months, results['Total_amt_per_order'].unique())
plt.xticks(months)
plt.ylabel('Sales in USD $')
plt.xlabel('Months')
plt.show()


# City with the best sales

# In[16]:


city_sales = all_data.groupby('City').sum()
city_sales.head(50)


# In[ ]:





# In[17]:


import matplotlib.pyplot as plt

cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, city_sales['Total_amt_per_order'])
plt.xticks(cities, rotation = 'vertical', size = 8)

plt.ylabel('Sales in USD $')
plt.xlabel('City name')
plt.show()


# Best time to display advertisement

# In[18]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# In[19]:


hours = [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours, size=8)
plt.grid()
plt.xlabel('Hours')
plt.ylabel('Number of orders')
plt.show()

#I recommend to advertise around 11:00 hrs and 18:00 hrs


# Products often sold together

# In[20]:


df = all_data[all_data['Order ID'].duplicated(keep = False)]

df ['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

df = df[['Order ID','Grouped']].drop_duplicates()

df.head(50)


# In[21]:


from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

count.most_common()    


# Product that got sold the most and reason

# In[22]:


all_data.head()


# In[23]:


best_selling_products = all_data.groupby('Product').sum()

best_selling_products.head(50)





# In[26]:


ordered_quantity = best_selling_products['Quantity Ordered']

products = [product for product, df in all_data.groupby('Product')]
plt.figure(figsize=(16,9))
plt.bar(products, ordered_quantity)
plt.xticks(products, rotation = 90, size = 12)
plt.yticks(best_selling_products['Quantity Ordered'])
plt.ylabel('Amount sold')
plt.xlabel('Product Names')
plt.show()


# In[27]:


prices = all_data.groupby('Product').mean()['Price Each']


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, ordered_quantity, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Products', color='g')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Prices of each products', color='g')
ax1.set_xticklabels(products, rotation = 90, size =8)
plt.show()


# In[ ]:




