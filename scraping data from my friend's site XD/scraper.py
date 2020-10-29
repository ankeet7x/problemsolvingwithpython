import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://sangamkhanal.com.np')
soup = BeautifulSoup(page.content, 'html.parser')

posts = soup.find_all(class_='post-list')
# postTitle = posts.find_all(class_='post-title')
# postDate = posts.find_all(class_='post-date')
# postBody = posts.find_all(class_='post')

postTitle = [post.find(class_='post-title').get_text() for post in posts]
postDate = [post.find(class_='post-date').get_text() for post in posts]
postBody = [post.find(class_='post').get_text() for post in posts]

# print(postTitle)

post_data = pd.DataFrame({
    'title': postTitle,
    'date': postDate,
    'body':postBody
})

print(post_data)
post_data.to_csv('data.csv')