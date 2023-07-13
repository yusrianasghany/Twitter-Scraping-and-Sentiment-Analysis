import tweepy
from textblob import TextBlob
from kafka import KafkaProducer
import json

def task():
   auth = tweepy.OAuthHandler('',
                              '')
   auth.set_access_token('',
                        '')

   producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda K: json.dumps(K).encode('utf-8'))

   api = tweepy.API(auth)
   cursor = tweepy.Cursor(api.search_tweets, q="polri kepolisian",tweet_mode='extended',lang='id').items(20)
   for tweet in cursor:
      producer.send('tugasde', tweet.full_text)
      data = json.dumps(str(tweet))
      print(tweet.full_text)