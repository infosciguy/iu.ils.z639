import re #import regular expressions
#
#
#
##Cleaning positive and negative word dictionaries#
def clean_lexicon_pos():
    positive_words = open("pos.wn", "r").readlines()
    new_pos_list = []
    for i in positive_words[:]:
        i = i.strip()
        i = re.sub("_", " ", i)
        new_pos_list.append(i)
    return new_pos_list
#
#
def clean_lexicon_neg():
    negative_words = open("neg.wn", "r").readlines()
    new_neg_list = []
    for i in negative_words[:]:
        i = i.strip()
        i = re.sub("_", " ", i)
        new_neg_list.append(i)
        return new_neg_list
#
#
##DICT NAMES##
positive_words = clean_lexicon_pos()
#
#
#negative_words = clean_lexicon_neg()
#
#print(positive_words[:]) #use this to print the positive word dictionary
#
#print(negative_words[:]) #use this to print the negative word dictionary
#
#
#We are going to use the pos/neg word dictionaries to determine the percentages of positive, negative and ambigious
#tweets in our txt file.
#
#
tweets = open("posTweets.txt", "r", encoding="UTF-8").readlines()
#
pos_counter=0
#
#
x = []  # positive tweets
y = []  # negative tweets
z = []  # ambiguous tweets
#
#
for line in tweets:
    for entry in positive_words:
        if entry in line and "not" not in line:
            pos_counter += 1
    if pos_counter > 1:
        x.append(entry)
        print(len(x), "Positive Tweet")
#
    else: pos_counter =0
    z.append(entry)
    print(len(z), "Ambiguous Tweet")
    if pos_counter < 0:
        print(len(y), "Negative Tweet")
    pos_counter=0
#
#
#NEXT STEPS: Count the total number of tweets, the number of tweets in each list x, y, z, and determine percentages of
#each relative to the total number of tweets in the txt file. Also, for each ambigious tweet, have python print its
#contents so it can be determined to be positive or negative
