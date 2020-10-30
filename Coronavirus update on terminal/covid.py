import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

list = []
yo = soup.find_all(class_='maincounter-number')

# data = pd.DataFrame({
#     'yo':yo
# })
for cases in yo:
    list.append(cases.get_text())

totalCases, totalDeaths, totalRecovered = list

print(f'total cases: {totalCases}')
print(f'total deaths: {totalDeaths}')
print(f'total recovered: {totalRecovered}')


# print(data)
# print(yo)

# print(yo.get_text())