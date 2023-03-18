from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

class Autorsvp():
	def __init__(self,email,password):

		self.browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
		self.browser.get("https://www.meetup.com")

		self.email = email
		self.password = password
	
	def login_with_email(self):
		
		sleep(5)

		login_button = self.chrome_browser.find_element(By.XPATH,'//*[@id="login-link"]')
		login_button.click()
		
		sleep(6)

		email_box = self.chrome_browser.find_element(By.ID,"email")
		email_box.send_keys(self.email)

		sleep(6)

		password_box = self.chrome_browser.find_element(By.ID,"current-password")
		password_box.send_keys(self.password)
		
		sleep(6)

		login_button = self.chrome_browser.find_element(By.NAME,"submitButton")
		login_button.click()

		sleep(15)





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

	email = 'Your Email'
	password = 'Your Password'

	groups = []

	waitTime = 60  #60 Minutes


	while True:
		# Run this every 1 hour
		
		rsvper = Autorsvp(email,password)
		rsvper.login_with_email()

		# Setup Browser
		


		# Login

		# Get Groups Details

			# Iterate through all events in groups

				# RSVP

		
		sleep(waitTime*60)

