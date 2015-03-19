# In the name of GOD!
# logging in with requests, scrolling & scraping

import re
import requests
from bs4 import BeautifulSoup as BS


def get_tweets(n_scrolls, user_name, auth):

    requests.packages.urllib3.disable_warnings()
    n = n_scrolls

    params = {}
    header = {'Cookie': 'auth_token=' + auth}
    url = 'https://twitter.com/' + user_name

    while n > 0:

        scrolled_page = requests.get(url, headers=header, params=params)

        new_soup = BS(scrolled_page.content)
        try:
            items = new_soup.find_all('div', {'class': 'GridTimeline-items'})[0]
        except IndexError:
            break
        tweets = items.find_all('p', {'class': 'ProfileTweet-text'})

        for tweet in tweets:
            yield tweet.text

        n -= 1

        try:
            max_id_temp = re.findall('max-id.+', scrolled_page.content)[0]
        except IndexError:
            break
        idx_temp = max_id_temp.find('"')
        max_id = max_id_temp[idx_temp+1: max_id_temp.find('"', idx_temp+1)]

        params = {'contextual_tweet_id': max_id,
                  'include_available_features': '1',
                  'include_new_items_bar': 'true',
                  'include_entities': '1',
                  'max_id': max_id}


def get_followers(user_name, auth):

    requests.packages.urllib3.disable_warnings()

    followers_list = []
    url = 'https://twitter.com/' + user_name + '/followers'
    header = {'Cookie': 'auth_token=' + auth}
    followers_page = requests.get(url, headers=header)

    soup = BS(followers_page.content)
    try:
        items = soup.find_all('div', {'class': 'GridTimeline-items'})[0]
    except IndexError:
        yield None

    followers = items.find_all('a', {'class': 'ProfileCard-avatarLink'})

    for f in followers:
        followers_list.append(f['href'][1:])
        yield f['href'][1:]


def get_following(user_name, auth):

    requests.packages.urllib3.disable_warnings()

    followers_list = []
    url = 'https://twitter.com/' + user_name + '/following'
    header = {'Cookie': 'auth_token=' + auth}
    followers_page = requests.get(url, headers=header)

    soup = BS(followers_page.content)
    try:
        items = soup.find_all('div', {'class': 'GridTimeline-items'})[0]
    except IndexError:
        yield None

    followers = items.find_all('a', {'class': 'ProfileCard-avatarLink'})

    for f in followers:
        followers_list.append(f['href'][1:])
        yield f['href'][1:]

