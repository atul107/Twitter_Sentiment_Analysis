# -*- coding: utf-8 -*-
"""
Created on Fri May 10 05:49:38 2019

@author: atk
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = "1126006627360919554-O8SEeivP8x980NsoY5QhnAFr3aAd7A"
access_token_secret =  "bCDov02FmtF9shlCTNJv0WxxlMNKsFhPYn7SlE1TlTtEm"
consumer_key =  "Em2AcTwsqhR6XMcymOARaUej0"
consumer_secret =  "wzblehM8zm3qk6t0jgRzGqvA4KOxkDt03aEB2HGxdyeGOPhxPm"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")