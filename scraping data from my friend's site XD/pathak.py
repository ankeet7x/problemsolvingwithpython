import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://saurabpathak.com.np')
soup = BeautifulSoup(page.content, 'html.parser')

postList = soup.find_all(class_='post-preview')
# print(postList)

postTitle = [post.find(class_='post-title').get_text() for post in postList]
postDate = [post.find(class_='post-meta').get_text() for post in postList]
postBody = [post.find(class_='post-entry').get_text() for post in postList]

post_data = pd.DataFrame({
    'title': postTitle,
    'date': postDate,
    'body': postBody
})

post_data.to_csv('pathak.csv')