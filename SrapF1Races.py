#!/usr/bin/env python
# coding: utf-8

# In[27]:


from bs4 import BeautifulSoup
import pandas as pd
with open('C:\\Users\\tibco\\Downloads\\2022 RACE RESULTS.html','r',encoding='utf8') as html_file:
    content = html_file.read()


# In[ ]:





# In[21]:


soup = BeautifulSoup(content,'lxml')


# In[25]:


tags = soup.find('table',{"class": "resultsarchive-table"})
headers = []
for i in tags.find_all('th'):
    tittle = i.text
    headers.append(tittle)


# In[35]:


mydata = pd.DataFrame(columns = headers)

for j in tags.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row
    
print(mydata)

