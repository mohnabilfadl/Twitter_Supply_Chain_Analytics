import re
import pandas as pd


# Function to clean tweets
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


df = pd.read_csv('supply_chain.csv')

df['text'] = df['text'].astype(str).apply(clean_tweet)

df.to_csv('supply_chain.csv', encoding='utf-8', index=False)
