import math
import pandas as pd
import numpy as np
import string
import nltk
from nltk import tokenize
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#%%
# open files downloaded from the discussion board
jd = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/jiefu dong.txt")
hl = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/han luo.txt")
zxx = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/zhixuan xia.txt")
tyy = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/tianyi yang.txt")
mgg = open("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/mengge geng.txt")

#to split name and purpose into two different list
def wrap_business(hw):
    result = list()
    for line in hw.readlines():
        for c in line:
            #remove unnecessary punctuation
            if (c in string.punctuation) and (c != "-"):
                line = line.replace(c, " ")
                line = line.strip()
        result.append(line)
    #print(result)
    name = list()
    purpose = list()
    for i in result:
        #find business names
        if i[0] == "N":
            a = i[5:]
            a = a.strip()
            name.append(a)
        #find business purpose
        elif i[0] == "P":
            b = i[8:]
            b = b.strip()
            purpose.append(b)
    return(name,purpose)



if __name__ == "__main__":
    content1 = wrap_business(jd)
    content2 = wrap_business(hl)
    content3 = wrap_business(zxx)
    content4 = wrap_business(tyy)
    content5 = wrap_business(mgg)
    business_name = content1[0] + content2[0] + content3[0] + content4[0] + content5[0]
    business_purpose = content1[1] + content2[1] + content3[1] + content4[1] + content5[1]


#%%
#to find best and worst description by using sentiment
def score(sentence):
    if type(sentence) != list:
        raise TypeError('Please input a list.')
    else:
        analyser = SentimentIntensityAnalyzer()
        score = list()
        for i in sentence:
            #score
            score_description = analyser.polarity_scores(i)
            #put score into a list
            score_comppound = score_description['compound']
            score.append(score_comppound)
        best = max(score)
        worst = min(score)
        print("The best score is:", best)
        print("The best sentence is:")
        for j in range(len(score)):
            if score[j] == best:
                print(sentence[j])
        print("\n")
        print("The worst score is:", worst)
        print("The worst sentence is:")
        for l in range(len(score)):
            if score[l] == worst:
                print(sentence[l])
        print("\n")

if __name__ == "__main__":
    score(business_purpose)


#%%
def get_tokens(details):
    if type(details) != list:
        raise TypeError("Please input a list.")
    else:
        ## transfer list to a string
        details_str = " ".join(details)
        #tokenize
        tokens = nltk.word_tokenize(details_str)
        #count value
        result = pd.value_counts(tokens)
        print("The 10 most common words/tokens in the description of the companies are:\n",result[0:10])

if __name__ == "__main__":
    get_tokens(business_purpose)



