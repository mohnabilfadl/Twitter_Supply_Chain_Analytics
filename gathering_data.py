# import libraries

import tweepy as tw
import json


# Function to work with th twiiter api

def get_api(consumer_key, consumer_secret, access_token,access_token_secret):
    """
    input: api credentials
    output: api

    """



    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    print("=================== api created =====================")
    return api

# Function to get twwets information from the api
def get_tweets(api, search_words = "#supplychain",  num_tweets=500):
    """
    input: search words , date , number of tweets and language
    output: json file of the information of tweets

    """
    print('=================== Start extracting ================')
    tweets = tw.Cursor( api.search_tweets,
                        q=search_words,
                        count=100,
                        ).items(num_tweets)

    # Iterate and print tweets
    list_tweet = [tweet._json for tweet in tweets]

    # save into json file 
    with open('tweets_info.json', 'w',encoding='utf-8') as f:
                json.dump(list_tweet, f, ensure_ascii=False, indent=4)
    print("=================== Saved done =====================")
    


    