# In the name of GOD!
# loging in with requests

import requests, re
from bs4 import BeautifulSoup as BS


def get_tweets(n_scrolls ,auth, user_name):

    requests.packages.urllib3.disable_warnings()

    tweets_list = []
    n = n_scrolls
    header = {'Cookie':'auth_token=' + auth}
    main_page = requests.get('https://twitter.com/' + user_name,
                             headers=header)
    soup = BS(main_page.content)
    items = soup.find_all('div', {'class':'GridTimeline-items'})[0]
    tweets = items.find_all('p', {'class':'ProfileTweet-text'})

    for tweet in tweets:
        print tweet.text, '\n'
        tweets_list.append(tweet.text)

    n -= 1

    max_id_temp = re.findall('max-id.+', main_page.content)[0]
    idx_temp = max_id_temp.find('"')
    max_id = max_id_temp[idx_temp+1:max_id_temp.find('"',idx_temp+1)]

    while n > 0:
        
        params = {'contextual_tweet_id':max_id,
          'include_available_features':'1',
          'include_new_items_bar':'true',
          'include_entities':'1',
          'max_id':max_id}

        scrolled_page = requests.get('https://twitter.com/' + user_name,
                             headers=header,
                             params=params)

        new_soup = BS(scrolled_page.content)
        items = new_soup.find_all('div', {'class':'GridTimeline-items'})[0]
        tweets = items.find_all('p', {'class':'ProfileTweet-text'})

        for tweet in tweets:
            print tweet.text, '\n'
            tweets_list.append(tweet.text)

        n -= 1
        
        max_id_temp = re.findall('max-id.+', scrolled_page.content)[0]
        idx_temp = max_id_temp.find('"')
        max_id = max_id_temp[idx_temp+1:max_id_temp.find('"',idx_temp+1)]

    for t in xrange(len(tweets_list)):      # Just for checking its correctness
        print t, tweets_list[t], '\n'       # when we want to use the function it must be replaced by return sth!!

get_tweets(5 ,'4d1c2137136cb297b3e83e382b0026d9213fe731', 'top_fash')
