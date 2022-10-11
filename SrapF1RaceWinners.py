#!/usr/bin/env python
# coding: utf-8

# In[52]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.formula1.com/en/results.html/2022/races.html'

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

tags = soup.find('table',{"class": "resultsarchive-table"})
headers = []
for i in tags.find_all('th'):
    tittle = i.text
    headers.append(tittle)
def func(value):
    return ' '.join(value.splitlines())
    
mydata = pd.DataFrame(columns = headers)
for i in range (1950,2023):
    url = 'https://www.formula1.com/en/results.html/'+str(i)+'/races.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    tags = soup.find('table',{"class": "resultsarchive-table"})
    for j in tags.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [func(i.text.strip()) for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row


print(mydata)
    
mydata.to_csv('C:\\Users\\tibco\\Downloads\\race_results.csv')

