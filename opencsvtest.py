
import csv
import collections
from collections import namedtuple

try:
    from itertools import imap
except ImportError:  # Python 3
    imap = map

with open(r"C:\Users\Jordan\Desktop\emot-tweets2.csv", mode="rt", encoding = "UTF-8") as infile:
    reader = csv.reader(infile)
    EmotionTweets = collections.namedtuple('tweetID', 'screenName, userName, tweet, noisy_label', rename=True)  # get names from column headers
    for data in imap(EmotionTweets._make, reader):
        print(EmotionTweets.tweet)
        # ...further processing of a line...

