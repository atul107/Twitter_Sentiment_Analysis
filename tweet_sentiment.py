# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:05:00 2019

@author: atk
"""
import json
from kafka import SimpleProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

#Token Keys to access Twitter
access_token = "1126006627360919554-O8SEeivP8x980NsoY5QhnAFr3aAd7A"
access_token_secret =  "bCDov02FmtF9shlCTNJv0WxxlMNKsFhPYn7SlE1TlTtEm"
consumer_key =  "Em2AcTwsqhR6XMcymOARaUej0"
consumer_secret =  "wzblehM8zm3qk6t0jgRzGqvA4KOxkDt03aEB2HGxdyeGOPhxPm"

es = Elasticsearch()

class StdOutListener(StreamListener):
    # on success
    def on_data(self, data):
        # decode json
        dict_data = json.loads(data)
        producer.send_messages("testTopic", data.encode('utf-8'))
        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])
        # output sentiment polarity
        print(tweet)
        print tweet.sentiment.polarity

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"
        # output sentiment
        print sentiment

        # add text and sentiment info to elasticsearch
        es.index(index="congress",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print status 
        
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="congress")