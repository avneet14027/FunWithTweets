# FunWithTweets

This repo consists of 3 files:
 - tweetExtract.py //extracting tweets using tweepy.Cursor()
 - tweetStreamExtract.py //extracting tweets from twitter stream
 - words.txt //words for which tweets will be extracted
 Using the two code files here I have demonstrated 2 different ways to achieve the task. The code has been developed and tested using Python 2.7.12 . The output is a hello.txt file which is a csv consisting of S.No, TweetID, TweetText.
 
 ### tweetExtract.py
 
#### Procedure

- Using Twitter Developer Platform, created an app and obtained access tokens and consumer tokens.
- Tweepy API in python is used.
- Authentication tokens (consumer as well as access) as well as the OAuthHandler are initialized.
- Words are read from the words.txt file and created into a query string, joined together by " OR " which is a logical OR operation to include all keywords
- Using the tweepy.Cursor() function, given the parameters as language="en", api.search, the query string and limit=10, the tweets are extracted, and stored in an array of theese tweet objects.
- Further these objects are then parsed for extracting their text and ID fields and he cleaned fields are stored into another array having each element as an array of the s.no, tweetID, tweetText .
- Finally, this array of cleaned objects is written rowwise into a csv file.

 ### tweetStreamExtract.py
 Here instead of using the tweepy.Cursor() command, one can get the real time stream by creating a Tweet Listener class to listen to incoming tweets. The limit is set to 5, since if too many requests are made for incoming tweets, then it is likely that we can see the 420 error code  which stands for the following:
 > *420
Rate Limited. Possible reasons are: Too many login attempts in a short period of time. Running too many copies of the same application authenticating with the same account name.*

#### Procedure

- Using Twitter Developer Platform, created an app and obtained access tokens and consumer tokens.
- Tweepy API in python is used.
- Authentication tokens (consumer as well as access) as well as the OAuthHandler are initialized.
- Words are read from the words.txt file and created into a query string, joined together by " OR " which is a logical OR operation to include all keywords
- A TwitterListener class is created whose instance is initialized as twitterStrea. The on_status function defines what to do in the even of a tweet which has been listened to. The on_error function helps us to detect errors by printing out the status messages. The tweets are stored as json objects in an array.
- Further these objects are then parsed for extracting their text and ID fields and he cleaned fields are stored into another array having each element as an array of the s.no, tweetID, tweetText .
- Finally, this array of cleaned objects is written rowwise into a csv file.

### Words.txt
Consists of words which would be used to extract tweets from twitter.
