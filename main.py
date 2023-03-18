from bs4 import BeautifulSoup
import requests



from time import sleep


#Fetchs links of events from group name
def fetch_events_by_group(group):

	group_link = f"https://www.meetup.com/{group}/events/"

	response = requests.get(group_link)

	if response.status_code != 200:
		print("Something Went Wrong! Please check Group Url")
		return []
	
	html_res = BeautifulSoup(response.text,"html.parser")
	events = html_res.select(".eventCard--link")
	events_links = [event.get("href") for event in events]

	return events_links

