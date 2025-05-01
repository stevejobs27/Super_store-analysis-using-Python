#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[42]:


df = pd.read_csv(r"C:\Users\sidda\Documents\projects\train.csv")
df.head()


# In[43]:


df.info()


# In[44]:


df.isnull().sum()


# In[45]:


df['Postal Code'].fillna(0,inplace = True)
df['Postal Code']=df['Postal Code'].astype(int)
df.info()


# In[46]:


df.describe()


# In[47]:


df.duplicated(keep = False).sum()


# In[ ]:





# # Exploratory Data Analysis
# 
# # Customer Analysis
# 
# # Customer Segmentation
# 
# 
# 

# 

# In[48]:


df.head(3)


# In[49]:


df['Segment'].unique()


# In[50]:


number_of_customers = df['Segment'].value_counts(ascending = True).reset_index()

number_of_customers = number_of_customers.rename(columns = {'index':'Customer Type','Segment':'Total Customers'})

number_of_customers


# In[51]:


plt.pie(number_of_customers['Total Customers'],labels = number_of_customers['Customer Type'],autopct = '%0.1f%%')

plt.title('Distrubution of Customers')
plt.show()


# In[ ]:





# In[ ]:





# # Sales per category

# In[52]:


sales_per_category = df.groupby('Segment')['Sales'].sum().reset_index()


sales_per_category =sales_per_category .rename(columns = {'Segment':'Customer Type','Sales':'Total Sales'})

sales_per_category


# In[53]:


plt.pie(sales_per_category['Total Sales'],labels =sales_per_category['Customer Type'],autopct = '%0.1f%%' )

plt.title('Sales per category')

plt.show()


# In[54]:


plt.bar(sales_per_category['Customer Type'],sales_per_category['Total Sales'])

plt.title('Sales per Category')

plt.xlabel('Sales')
plt.ylabel('Segment')

plt.show()


# In[ ]:





# In[55]:


df.head(3)


# In[ ]:





# In[ ]:





# # Customer Loyalty

# In[56]:


customer_order_freq = df.groupby(['Customer ID','Customer Name','Segment'])['Order ID'].count().reset_index()


customer_order_freq.rename(columns = {'Order ID' : 'Total Orders'},inplace = True)

repeat_customers = customer_order_freq[customer_order_freq['Total Orders'] >= 1]

sorted_repeat_customers = repeat_customers.sort_values(by = 'Total Orders',ascending = False)

print(sorted_repeat_customers.head(10).reset_index())


# In[57]:


# Total Sales


# In[58]:


customer_sales = df.groupby(['Customer ID','Customer Name','Segment'])['Sales'].sum().reset_index()

top_spenders = customer_sales.sort_values(by = 'Sales',ascending = False)

print(top_spenders.head(10).reset_index(drop = True))


# In[ ]:





# In[ ]:





# # Mode of Shipping

# In[59]:


df['Ship Mode'].unique()


# In[60]:


shipping_mode = df['Ship Mode'].value_counts(ascending = True).reset_index()

shipping_mode = shipping_mode.rename( columns = {'index' : 'Ship Mode','Ship Mode':'No of Shipments' })

print(shipping_mode)


# In[61]:


plt.pie(shipping_mode['No of Shipments'],labels = shipping_mode['Ship Mode'],autopct = '%0.1f%%')

plt.title('Mode of Shopping')

plt.show()


# In[62]:


state = df['State'].value_counts(ascending = False).reset_index()

state = state.rename( columns = {'index' : 'State Name', 'State':'No of Customers' })

print(state.head(10))


# In[63]:


state = df['City'].value_counts(ascending = False).reset_index()

state = state.rename( columns = {'index' : 'City', 'City':'No of Customers' })

print(state.head(10))


# In[64]:


state_sales = df.groupby(['State'])['Sales'].sum().reset_index()

sort_by_sales = state_sales.sort_values(by = 'Sales',ascending = False)

print(sort_by_sales.head(10).reset_index(drop = True))


# In[65]:


city_sales = df.groupby(['City'])['Sales'].sum().reset_index()

sort_by_sales = city_sales.sort_values(by = 'Sales',ascending = False)

print(sort_by_sales.head(10).reset_index(drop = True))


# In[ ]:





# # Product Analysis

# In[66]:


df.head(3)


# In[67]:


df['Category'].unique()


# In[68]:


sub_category = df.groupby(['Category'])['Sub-Category'].nunique().reset_index()


print(sub_category)


# In[69]:


sales_per_category = df.groupby(['Category'])['Sales'].sum().reset_index()

sales_per_category= sales_per_category.sort_values(by ='Sales',ascending = False)

print(sales_per_category.reset_index(drop=True))


# In[70]:


plt.pie(sales_per_category['Sales'],labels =sales_per_category['Category'],autopct = '%0.1f%%')

plt.title('Sales per category')

plt.show()


# In[71]:


sub_category_sales = df.groupby(['Sub-Category'])['Sales'].sum().reset_index()

sub_category_sales= sub_category_sales.sort_values(by ='Sales',ascending = False)

print(sub_category_sales.reset_index(drop=True))


# In[72]:


sub_category_sales = sub_category_sales.sort_values(by ='Sales',ascending = True)
plt.barh(sub_category_sales['Sub-Category'], sub_category_sales['Sales'])

plt.title('Sales for Sub category')
plt.xlabel('Sales')
plt.ylabel('Category')
plt.show()


# In[ ]:





# In[ ]:





# #  Trend Analysis

# In[89]:


df['Order Date']= pd.to_datetime(df['Order Date'],dayfirst = True)

yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()

yearly_sales = yearly_sales.reset_index()

yearly_sales =yearly_sales.rename(columns={'Order Date':'Year','Sales': 'Yearly Sales'})



print(yearly_sales)


# In[94]:



plt.bar(yearly_sales['Year'],yearly_sales['Yearly Sales'])

plt.title('Sales Per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.xticks(yearly_sales['Year'],rotation = 0)
plt.show()


# In[ ]:





# # Quaterly Sales
# 

# In[123]:


df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)

yearly_sales = df[df['Order Date'].dt.year == 2018]

Quarterly_sales = yearly_sales.resample('Q',on = 'Order Date')['Sales'].sum()

Quarterly_sales = Quarterly_sales.reset_index()

Quarterly_sales =Quarterly_sales.rename(columns={'Order Date':'Quarter','Sales': 'Quarter Sales'})


print(Quarterly_sales)


# In[126]:


plt.plot(Quarterly_sales['Quarter'], Quarterly_sales[ 'Quarter Sales'],marker = 'o',linestyle = '--')

plt.title('Sales Per Year')
plt.xlabel('Quarter')
plt.ylabel('Total Sales')
plt.xticks(Quarterly_sales['Quarter'])
plt.show()


# In[ ]:





# # Monthly Sales Trend

# In[156]:


df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)

yearly_sales = df[df['Order Date'].dt.year == 2018]

Monthly_sales = yearly_sales.resample('M',on = 'Order Date')['Sales'].sum()

Monthly_sales = Monthly_sales.reset_index()

Monthly_sales = Monthly_sales.rename(columns={'Order Date':'Month','Sales': 'Monthly Sales'})


print(Monthly_sales)


# In[160]:


plt.plot(Monthly_sales['Month'],Monthly_sales['Monthly Sales'],marker = 'o',linestyle = '-')

plt.title('Sales Per Year')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation = 65)
plt.show()


# In[ ]:





# In[ ]:




