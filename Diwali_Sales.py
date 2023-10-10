#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[39]:


all_data = pd.read_csv(r'C:\Users\asus\Downloads\Diwali Sales Data.csv',encoding='unicode_escape')
all_data.head()


# In[40]:


all_data.info()


# In[41]:


all_data.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[42]:


all_data.dropna(inplace=True)
all_data.isnull().sum()


# In[43]:


all_data.info()


# In[44]:


all_data['Amount']=all_data['Amount'].astype('int')


# In[45]:


all_data.columns


# In[58]:


all_data.rename(columns={'Cust_name':'Customer_name'}, inplace=True)


# In[49]:


all_data.describe()


# In[52]:


all_data[['Age','Orders','Amount']].describe()


# # Gender

# In[55]:


f_m = sns.countplot(x='Gender', data= all_data)

for bars in f_m.containers:
    f_m.bar_label(bars)


# In[64]:


#grouping by gender

Gender_groups = all_data.groupby(['Gender'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False)
sns.barplot(x='Gender', y='Amount', data=Gender_groups)


# Females have done more than double amount of shopping than men

# # Age

# In[67]:


Age_sales = sns.countplot(x='Age Group', hue= 'Gender',data= all_data)

for bars in Age_sales.containers:
    Age_sales.bar_label(bars)


# In[70]:


#by amount
Age_groups = all_data.groupby(['Age Group'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False)
sns.barplot(x='Age Group', y='Amount', data=Age_groups)


# From above graphs it is clear that age group of 26-35 years have spent the most and females have dominated it.

# # State

# In[84]:


#total number of orders from top 10 states

State_groups = all_data.groupby(['State'], as_index =False)['Orders'].sum().sort_values(by='Orders',ascending =False).head(10)
sns.set(rc={'figure.figsize':(16,9)})

sns.barplot(x='State', y='Orders', data=State_groups)
plt.xticks(rotation=70)
plt.show()


# In[87]:


#total Amount spent from top 10 states

Amt_groups = all_data.groupby(['State'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False).head(10)
sns.set(rc={'figure.figsize':(16,9)})

sns.barplot(x='State', y='Amount', data=Amt_groups)
plt.xticks(rotation=70)
plt.show()


# Most number of orders are from Uttar Pradesh, Maharashtra and Karnataka and they also top in purchasing power respectively

# In[93]:


Relationship = sns.countplot(x='Marital_Status', data= all_data)
sns.set(rc={'figure.figsize':(6,6)})
for bars in Relationship.containers:
    Relationship.bar_label(bars)


# In[101]:


Rel_status = all_data.groupby(['Marital_Status','Gender'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False).head(10)
sns.set(rc={'figure.figsize':(6,6)})

sns.barplot(x='Marital_Status', y='Amount', hue='Gender' ,data=Rel_status)



# Both married and unmarried females have shown more purchasing power. For men it is more or less the same.

# # Occupation 

# In[111]:


Occupation_group = sns.countplot(x='Occupation', data= all_data)
sns.set(rc={'figure.figsize':(16,9)})
for bars in Occupation_group.containers:
    Occupation_group.bar_label(bars)
plt.xticks(rotation=25, size = 10)
plt.show()


# In[117]:


Occupation_power = all_data.groupby(['Occupation'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False)
sns.set(rc={'figure.figsize':(16,9)})
sns.barplot(x='Occupation', y='Amount' ,data=Occupation_power)
plt.xticks(rotation=25, size = 10)
plt.show()


# # Product catagory

# In[124]:


Products = sns.countplot(x='Product_Category', data= all_data)
sns.set(rc={'figure.figsize':(16,2)})
for bars in Products.containers:
    Products.bar_label(bars)
plt.xticks(rotation=65, size = 10)
plt.show()


# In[125]:


Product_power = all_data.groupby(['Product_Category'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending =False)
sns.set(rc={'figure.figsize':(16,9)})
sns.barplot(x='Product_Category', y='Amount' ,data=Product_power)
plt.xticks(rotation=25, size = 10)
plt.show()


# Number of orders is topped by Clothing & Apparel followed by food and electronics and gadgets. But the amount spent in catagories are topped by Food followed by Clothing & Apparel and Electronics & Gadgets

# # #most sold products

# In[126]:


all_data.columns


# In[134]:


Product_id = all_data.groupby(['Product_ID'], as_index =False)['Orders'].sum().sort_values(by='Orders', ascending =False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID', y='Orders' ,data=Product_id)
plt.xticks(rotation=25, size = 10)


# In[138]:


all_data['Product_ID']('
                       ')

