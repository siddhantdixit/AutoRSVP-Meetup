# AutoRSVP Meetup

The “Auto RSVP Meetup” bot is a command-line tool built using Selenium with Python. It is designed to help users automatically sign up for events in specific Meetup groups. Before running the bot, users can configure which Meetup groups the bot should search for events in. The bot then takes care of authentication and searches for events in these configured groups on the user’s behalf. It uses Selenium to interact with the Meetup website and automatically sign up for these events in a timely manner to ensure that the user gets a spot. The bot can be run from cron at a desired frequency, such as once an hour (60 minutes). This means that if a new event is added to one of the configured Meetup groups within that hour, the bot will automatically RSVP for that event on the user’s behalf during its next run.

## Images


## Requirements
Tested successfully in the following environment.

- Python 3.10.6
- Selenium 4.8.2
- Ubuntu 22
- Firefox 111.0 (Mozilla Firefox Snap for Ubuntu)

## Setup
1. Clone the AutoRSVP Meetup repository
```
git clone 
cd 
```
2. Install the required Python libraries using the below command 
```
pip3 install -r requirements.txt
```
4. Run the bot 
```
python3 main.py
```
5. Enter your Meetup Email and Password with the groups that you need to RSVP's events of (Note- You should have joined the group on Meetup in case the group is not public) 


