#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.formula1.com/en/results.html/1975/races/346/south-africa/fastest-laps.html'

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

tags = soup.find('table',{"class": "resultsarchive-table"})
headers = []
for i in tags.find_all('th'):
    tittle = i.text
    headers.append(tittle)

headers.append('date')
headers.append('circuit')

  
mydata = pd.DataFrame(columns = headers)

print(mydata)

def func(value):
    return ' '.join(value.splitlines())

for i in range (2021,2023):
    url = 'https://www.formula1.com/en/results.html/'+str(i)+'/races.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    tags = soup.find_all('a',{"class": "dark bold ArchiveLink"})
    for j in tags:
        url1 = 'https://www.formula1.com/' +  j['href']
        url = url1.replace('race-result.html','fastest-laps.html')
        
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
mydata.to_csv('C:\\Users\\tibco\\Downloads\\fastest_laps.csv')

