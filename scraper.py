from lxml import html
import requests
import os.path
import json
import tweepy
import secrets

# Twitter auth
auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)
api = tweepy.API(auth)

# Web scraping
page = requests.get('https://fieldworkbrewing.com/berkeley/')
tree = html.fromstring(page.content)

current_beer = tree.xpath('//ul[@class="taplist-content"]//li[@class="beer ontap "]//div[@class="beer-content"]')

# If JSON exists, is opened and put in old_beers
old_beers = []
if os.path.isfile("beers.json"):
  old_beers = json.load(open('beers.json'))

vowels = ('A', 'E', 'I', 'O', 'U')
name_list = []
for beer in current_beer:
  # Names and descriptions taken from website
  name = beer.xpath('h1/text()')[0]
  description = beer.xpath('h2/text()')[0]
  if name not in old_beers:
    # Names not found in old_beers tweeted with vowel handling
    if description.startswith(vowels):
      api.update_status(f'NEW BEER ALERT: {name} is an {description}!!!')
    else:
      api.update_status(f'NEW BEER ALERT: {name} is a {description}!!!')
    print("NEW BEER OH SHIT")
  name_list.append(name)

# Beer JSON either overwritten or created
with open('beers.json', 'w') as outfile:
  json.dump(name_list, outfile)

print("AYYYYYY")

