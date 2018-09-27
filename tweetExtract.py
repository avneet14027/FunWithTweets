"""
  @Avneet Kaur
  Getting tweets containing specific keywords out of a twitter

"""

# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import csv
import HTMLParser

consumerKey = "zSEPmNwzvzyzeEb29kDhQAzXm"
consumerSecret = "sFS0hAW5VwPf6ODgc6AbjRjPki3irThlRAnsxAEoA3JxZPEF12"
accessKey = "1017803951431979009-9IGD4BeBFSEOmU0nRJBodZJ5ick7an"
accessSecret = "23WAzOi2ECZwJuFOEEc5L3Rz8P1ODxUZWL2LxNchGyxUu"

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)

tweetObjects = []

#get tweets
def getTweets(auth,query,language,limit):
  global tweetObjects
  api = tweepy.API(auth)
  for tweet in tweepy.Cursor(api.search, q=query, lang=language).items(limit):
    tweetObjects.append(tweet)

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
  limit = 100
  language = "en"
  query = ""
  
  #get query from file
  words = readQueryTerms("words.txt") 
  words = [x.lower().strip() for x in words]
  query = (" OR ").join(words)
  
  cleanedTweets = parseJSON(tweetObjects)
  writeToCSV(cleanedTweets,"out.txt")
