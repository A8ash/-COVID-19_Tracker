import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(html)
s= soup.find('table',attrs={"id":"main_table_countries_today"})

rows=s.find_all('tr')
#تشيل المسافات
rows[0].text.strip().split('\n')
#لوب بناء الحدول
data =[]
for row in rows:
    data.append(row.text.strip().split('\n')[1:5])
#نحولها الى جداول بستخدام pd

df=pd.DataFrame(data[9:240],columns=data[0])
#هنا نشيل البيانات للي مالها لازمه
#df.info()
df.drop('NewCases',axis=1,inplace=True)
#نحفظ على نفس العامود عشان لا تتغير علينا البيانات
df['TotalCases']= df['TotalCases'].str.replace(',','')
df['TotalCases'].str.replace(',','')
