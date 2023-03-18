from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

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



if __name__ == "__main__":

	email = 'dixit.rishu00@gmail.com'
	password = 'rishudixit2023'

	groups = []

	waitTime = 60  #60 Minutes


	while True:
		# Run this every 1 hour

		# Setup Browser

		# Login

		# Get Groups Details

			# Iterate through all events in groups

				# RSVP

		
		sleep(waitTime*60)

