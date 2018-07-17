from lxml import html
import requests
import os.path
import json
import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

page = requests.get('https://fieldworkbrewing.com/berkeley/')
tree = html.fromstring(page.content)

current_beer = tree.xpath('//ul[@class="taplist-content"]//li[@class="beer ontap "]//div[@class="beer-content"]')

# name = all_beer[0].xpath('h1/text()')[0]

# description = tree.xpath('//ul[@class="taplist-content"]//li[@class="beer ontap "]//div[@class="beer-content"]//h2/text()')

# description = all_beer[0].xpath('h2/text()')[0]

# https://doc.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html
# https://3583bytesready.net/2016/08/17/scraping-data-python-xpath/

old_beers = []
if os.path.isfile("beers.json"):
  old_beers = json.load(open('beers.json'))

# old_beers = ["Doge", "Nyancat", "Cherry Parfait", "Cloud Control", "End of Years", "Favourite Melodies", "Field Trial Series", "Dickbutt", "Ghost of a Hop", "Hacking the Mainframe", "In Bloom", "Kolsch City Rockers", "Mount Sierra", "Past The Breakers", "Simple Joys", "Where Belges Dare"]

name_list = []
for beer in current_beer:
  name = beer.xpath('h1/text()')[0]
  description = beer.xpath('h2/text()')[0]
  if name not in old_beers:
    api.update_status(f'NEW BEER ALERT: {name} is a {description}!!!')
  name_list.append(name)

# json_attempt = json.dumps(name_list)
# print(json_attempt)

with open('beers.json', 'w') as outfile:
  json.dump(name_list, outfile)

