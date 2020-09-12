import os
import time
import tweepy
import subprocess
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
key = "key"
secret = "secret"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
bscr = 'for i in $(shuf -i 1-280);do echo -n "$(shuf chars -n 1)";done'

while True:
    text = subprocess.check_output(bscr, shell=True)
    print(text)
    api.update_status(text)
    time.sleep(25)
