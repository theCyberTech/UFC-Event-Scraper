# Name : ufc_scraper.py v0.0.1
# Author : thCyberTech
# Date : 12th Jan 2022
# Description : A class based python file that scrapes the UFC website for the latest events

import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self):
        
        self.url = "https://www.ufc.com/events"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.results = self.soup.find(id="events-list-upcoming")
        self.upcoming_events = self.results.find_all("div", class_="c-card-event--result__info")
        self.event = None
        self.fight = None
        self.fight_time_main = None
        self.fight_location = None

    def get_tags(self):
        
        for self.event in self.upcoming_events:
            self.fight = self.event.find("h3", class_="c-card-event--result__headline")
            self.fight_time_main = self.event.find("div", class_="c-card-event--result__date tz-change-data")
            self.fight_location = self.event.find("div", class_="field field--name-taxonomy-term-title field--type-ds field--label-hidden field__item")
            
            print(f'Main Event: {self.fight.text.strip()}')
            print(f'Date: {self.fight_time_main.text.strip()}')
            print(f'Location: {self.fight_location.text.strip()}')
            print()

def main():

    s = Scraper()
    s.get_tags()

if __name__ == '__main__':
    main()