from collections import defaultdict
import numpy as np
from random import shuffle, randint

#############
#####OPEN AND READ THE FILE#####
##########
alldata = open (r'C:\Users\Jordan\Desktop\emot-tweets.csv', encoding = "UTF-8")
mylist = alldata.readlines()
#split and lowercase data
for line_no, line in enumerate(mylist):
        label = line.split()[0]
        word_list = line.lower().split()[3:]

#print(mylist)

h = [] #HAPPY TWEETS
s = [] #SAD TWEETS

for line in mylist:
        if "HAPPY" in line:
            h.append(line)    # 1 is the label for happy
        elif "SAD" in line:
            s.append(line)    # 2 is the label for sad
#print(h)
print(s[5])
#end



print("There are", len(s), "sad tweets")

print("There are", len(h), "happy tweets")

###above this line is good###

##separate into training & testing data##

happy_train_data = h[:200]
#
happy_test_data = h[:200:350]
#
sad_train_data = s[:1000]
#
sad_test_data = s[1000:2000]
#########
#above this line good
##########

def get_space(happy_train_data):
    word_space=defaultdict(int)
    for doc in happy_train_data:
        for w in doc.words:
            word_space[w]=len(word_space)
        return word_space

word_space = get_space(happy_train_data)
#print (len(word_space))

def get_space(sad_train_data):
    word_space=defaultdict(int)
    for doc in happy_train_data:
        for w in doc.words:
            word_space[w]=len(word_space)
        return word_space
#
#Sparse vector creation
#
def get_sparse_vec(data_point, space):
    sparse_vec = np.zeros((len(space)))
    for w in set(data_point.words):
        try:
            sparse_vec[space[w]] = 1
            except:
                continue
            return sparse_vec
