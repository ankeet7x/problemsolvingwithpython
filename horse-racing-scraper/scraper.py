import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.punters.com.au/form-guide/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

tracks = soup.find_all(class_="upcoming-race__row")

# trackName = [track.find(class_="upcoming-race__event-link upcoming-race__event-link--resulted") for track in tracks]

# race1 = [track.find(class_="upcoming-race__event-link upcoming-race__event-link--resulted").get_text() for track in tracks]
# print(race1)

R1 = []
for track in tracks:
	text = track.find(class_="upcoming-race__event-link upcoming-race__event-link--resulted")
	if text is not None:
		race1 = text.get_text()
		R1.append(race1)
	# else:
	# 	R1.append("None")

# R2 = []
# for track in tracks:
# 	text = track.find(class_="upcoming-race__event-link upcoming-race__event-link--resulted")
# 	if text is not None:
# 		race2 = text.get_text()
# 		R2.append(race2)
print(R1)
# print(R2)