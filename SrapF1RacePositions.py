#!/usr/bin/env python
# coding: utf-8

# In[27]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.formula1.com//en/results.html/2022/races/1124/bahrain/race-result.html'

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

tags = soup.find('table',{"class": "resultsarchive-table"})
headers = []
for i in tags.find_all('th'):
    tittle = i.text
    headers.append(tittle)

headers.append('date')
headers.append('circuit')

def func(value):
    return ' '.join(value.splitlines())
    
mydata = pd.DataFrame(columns = headers)

print(mydata)
for i in range (1950,2023):
    url = 'https://www.formula1.com/en/results.html/'+str(i)+'/races.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    tags = soup.find_all('a',{"class": "dark bold ArchiveLink"})
    for j in tags:
        url = 'https://www.formula1.com/' +  j['href']
        detailpage = requests.get(url)
        standings = BeautifulSoup(detailpage.text,'lxml')
        table = standings.find('table',{"class": "resultsarchive-table"})
        date = standings.find('span',{"class":"full-date"}).text
        circuit = standings.find('span',{"class":"circuit-info"}).text
        for k in table.find_all('tr')[1:]:
            row_data = k.find_all('td')
            row = [func(l.text.strip()) for l in row_data]
            row.insert(-1,date)
            row.insert(-1,circuit)
            length = len(mydata)
            mydata.loc[length] = row
        

print(mydata)
mydata.to_csv('C:\\Users\\tibco\\Downloads\\race_positions.csv')

