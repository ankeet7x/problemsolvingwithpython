import requests
from bs4 import BeautifulSoup
import pandas as pd



def covidInquiry(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    list = []
    allData = soup.find_all(class_='maincounter-number')


    for cases in allData:
        list.append(cases.get_text())

    totalCases, totalDeaths, totalRecovered = list

    print(f'total cases: {totalCases}')
    print(f'total deaths: {totalDeaths}')
    print(f'total recovered: {totalRecovered}')


print("Do you want to view global data or country data ?\n")
check = input("Type global for global data or country name for country data\n")

if check == 'global':
    url = 'https://www.worldometers.info/coronavirus/'
else:
    url = f'https://www.worldometers.info/coronavirus/country/{check}'


covidInquiry(url)





