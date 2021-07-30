import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.racenet.com.au/results/horse-racing"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="latest-result-row")

raceNumber = [result.find(class_="latest-result-row__race-number").get_text() for result in results]
raceLocation = [result.find(class_="latest-result-row__location").get_text() for result in results]
raceState = [result.find(class_="latest-result-row__state").get_text() for result in results]
raceResult = [result.find(class_="resulted-selections__container").get_text() for result in results]
raceDistance = [result.find(class_="latest-result-row__distance").get_text() for result in results]
raceResultStatus = [result.find(class_="latest-result-row__status").get_text() for result in results]

formatted_race_distance = [race.replace("\n", "") for race in raceDistance]
formatted_race_location = [race.replace("\n", "") for race in raceLocation]
formatted_race_result = [race.replace("\n", "") for race in raceResult]
formatted_result_status = [race.replace("\n", "") for race in raceResultStatus]
formatted_race_state = [race.replace("\n", "") for race in raceState]


race_data = pd.DataFrame({
	"Race Number": raceNumber,
	"Race Location": formatted_race_location,
	"Race State": formatted_race_state,
	"Race Result": formatted_race_result,
	"Race Distance": formatted_race_distance,
	"Race result status": formatted_result_status
	})

race_data.to_csv("race_result.csv")