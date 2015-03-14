import urllib2
from bs4 import BeautifulSoup as BS

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'auth_token=4d1c2137136cb297b3e83e382b0026d9213fe731'))
page_contents = opener.open('https://twitter.com/shamgholi_hadi')   # or https://twitter.com/adidassoccer  or s.th else.

soup = BS(page_contents)

items = soup.find_all('div', {'class':'GridTimeline-items'})[0]

tweets = items.find_all('p', {'class':'ProfileTweet-text'})
tweet_counter = len(tweets) 

for item in tweets:
    print tweet_counter, ':', item.text, '\n'
    tweet_counter -= 1

def tweet_scraper(url):
    
    page_contents = opener.open(url)

    soup = BS(page_contents)
    items = soup.find_all('div', {'class':'GridTimeline-items'})[0]
    tweets = items.find_all('p', {'class':'ProfileTweet-text'})

    for item in tweets:
        yield item.text     #returns constructor. it must be used in a loop!!

for tweet in tweet_scraper('https://twitter.com/BlaiseHoney'):
    print tweet, '\n'
