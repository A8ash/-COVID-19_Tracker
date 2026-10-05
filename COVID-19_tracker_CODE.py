import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(html, 'html.parser')
s = soup.find('table', attrs={"id":"main_table_countries_today"})

rows = s.find_all('tr')
# تشيل المسافات
rows[0].text.strip().split('\n')
# لوب بناء الجدول
data = []
for row in rows:
    data.append(row.text.strip().split('\n')[1:5])
# نحولها الى جداول باستخدام pd

df = pd.DataFrame(data[9:240], columns=data[0])
# هنا نشيل البيانات اللي مالها لازمه
# df.info()
df.drop('NewCases', axis=1, inplace=True)

# تنظيف وتجهيز الأعمدة بشكل آمن
df['TotalCases'] = df['TotalCases'].str.replace(',', '').str.strip()
df['TotalCases'] = pd.to_numeric(df['TotalCases'], errors='coerce').fillna(0).astype(int)

df['TotalDeaths'] = df['TotalDeaths'].str.replace(',', '').str.strip()
df['TotalDeaths'] = pd.to_numeric(df['TotalDeaths'], errors='coerce').fillna(0).astype(int)

print(df)
# استخراج البيانات الى CSV
df.to_csv('data.csv', index=False)
print(df.columns)

# رسم بياني لأعلى 15 دولة لتجنب ازدحام الرسم
df.head(15).plot(kind='bar', x='Country,Other', y='TotalCases')
plt.show()