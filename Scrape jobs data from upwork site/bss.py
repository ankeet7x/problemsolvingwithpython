import requests
from bs4 import BeautifulSoup


url = 'https://www.upwork.com/ab/find-work/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


postList = soup.find_all(class_='job-title-link')
# postList = soup.find_all(data-job_= "job")
print(postList)