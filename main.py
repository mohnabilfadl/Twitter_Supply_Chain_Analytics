from  gathering_data import get_api, get_tweets
from processing import connect, process


consumer_key= 
consumer_secret= 
access_token= 
access_token_secret= 

api = get_api(consumer_key, consumer_secret, access_token,access_token_secret)
get_tweets(api)
connection = connect()
process(connection)