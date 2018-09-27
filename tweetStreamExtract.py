"""
@Avneet Kaur

Getting tweets containing specific keywords out of a twitter stream

"""
# -*- coding: utf-8 -*-
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import HTMLParser
import csv

consumerKey = "uCsPigNph7jucTr0JIGRdvD7Z"
consumerSecret = "WLSkdDpXUcUYOeU2puk3Q1uQKidURMd18kjNMGKWIVasnXLx1A"
accessKey = "1017803951431979009-mYwKyFpi0wrETuT21t28gmHtdaGAKf"
accessSecret = "JSBlFd4fVPAK7VfzIOvtVxeAl4HrF9FjZ8hOKFT3qb9D9"

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)

tweetObjects = []

class TweetListener(StreamListener):
  
  def __init__(self):
    super(TweetListener, self).__init__()
    self.counter = 0
    self.limit = 5
        
  def on_status(self,data):
    global tweetObjects
    tweetObjects.append(data)
    self.counter += 1
    if self.counter < self.limit:
      return True
    else:
      twitterStream.disconnect()
  def on_error(self,status):
    	print(status)
    	
#clean the tweets by removing html characters like "&lt; &amp;" from tweets
def cleanText(tweet):
  parser = HTMLParser.HTMLParser()
  tweet = parser.unescape(tweet) 
  tweet = tweet.encode('ascii', 'ignore')
  return tweet

#parse the tweet object to extract text and id
def parseJSON(tweetObjects):
  tweetsCleaned = []
  counter = 1
  for tweet in tweetObjects:
    tweet_id = tweet.id_str
    tweet_text = cleanText(tweet.text)
    tweetsCleaned.append([counter,tweet.id_str,tweet_text])
    counter+=1
  return tweetsCleaned

#write the cleaned tweets to csv file
def writeToCSV(tweets,filename):
  with open(filename, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for tweet in tweets:
      wr.writerow([tweet[0]] + [tweet[1]] + [tweet[2]])

#read file to get query terms
def readQueryTerms(filename):
  with open(filename) as f:
    lines = f.readlines()
  return lines
    	
if __name__ == "__main__":

  #get query words
  words = readQueryTerms("words.txt") 
  words = [x.lower().strip() for x in words]

  #get twitter stream
  twitterStream = Stream(auth, TweetListener())
  twitterStream.filter(track=words)

  #get cleaned tweets
  cleanedTweets = parseJSON(tweetObjects)
  writeToCSV(cleanedTweets,"output.csv")


