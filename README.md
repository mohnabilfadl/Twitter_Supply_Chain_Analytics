# Supply Chain Analytics

Supply Chain Analytics is the process of evaluating every stage of a supply chain starting from the time the business acquires raw materials or supplies from its suppliers to the delivery of final products to the customers.

![image](https://www.mytechmag.com/wp-content/uploads/2020/05/supply-chain-analytics.jpg)



## Pipeline:-

- Data Gathering.
- Data Cleaning.
- Data processing.
- Data storing in mongodb.
- Data Visualization using PowerBI.



## Data Gathering:-

Getting data from twitter api tweepy

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


## Data Cleaning:-

    def clean_tweet(text):  

        """
        input: tweet
        output: cleaned tweet

        """
        text = text.lower()    
        text = re.sub('https?://[A-Za-z0-9./]+', ' ', text)   #remove url links
        text = re.sub("www.[A-Za-z0-9./]+", ' ', text)        #remove url links
        text = re.sub('@[^\s]+', ' ', text)     #remove user name
        text = re.sub('\d+', ' ', text)         #remove digits
        text = re.sub(r'[^\w\s]+', ' ', text)   #remove punctuations
        text = re.sub('_+', ' ', text)          #remove _ char
        text = re.sub('\n', ' ', text)          #convert to one line only
        text = re.sub(r'\b\w{1,2}\b', '', text) #remove words < 2
        text = re.sub(' +', ' ', text)          #convert two or more spaces into one space
        return text
        
        
## Data processing:-

        def process(collection, file='tweets_info.json'):
    """
    input: json file
    output: updated mongo database 

    """
    with open(file, 'r', encoding="utf-8",) as json_file:
        json_load = json.load(json_file)

    print("=================== Opening success ===================")
    
    for data in json_load:
        mongo_data = {}
        mongo_data['created_at'] = data['created_at']
        mongo_data['text'] = data['text']
        mongo_data['lang'] = data['lang']
        mongo_data['retweet_count'] = data['retweet_count']
        mongo_data['favorite_count'] = data['favorite_count']
        mongo_data['user_name'] = data['user']['name']
        mongo_data['user_descreption'] = data['user']['description']
        mongo_data['user_followers_count'] = data['user']['followers_count']
        mongo_data['user_friends_count'] = data['user']['friends_count']
        mongo_data['user_favourites_count'] = data['user']['favourites_count']
        mongo_data['user_location'] = data['user']['location']
        collection.insert_one(mongo_data)    

    print('=================== database updated ===================')
    
## Data storing in mongodb:-

![image](https://user-images.githubusercontent.com/63733989/174310699-7ef7311b-5fe5-4cb0-a9a4-f17806b203a5.png)

## Data Visualization using PowerBI:-

![image](https://user-images.githubusercontent.com/63733989/174310835-bec52dc2-9fca-455b-bc30-544dd889b4ac.png)




