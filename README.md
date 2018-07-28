# beerbot

A little Twitter bot that tweets when new beers are on tap at Fieldwork Brewing at Berkeley.

[See my Medium post about building this project!](https://medium.com/@cfuj/beer-bot-101-making-twitter-better-one-beer-alert-at-a-time-56c8eae09f93)

## Built With

* Python 3.6
* LXML
* Tweepy (only works with Python 3.6)

## Please Note

The scraper.py file is importing a secrets.py file that is not in this repo. Get your own Twitter auths on Twitter.com.

My secrets.py file looks like:

```
access_token = "long auth string"
access_token_secret = "long auth string"
consumer_key = "long auth string"
consumer_secret = "long auth string"
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
