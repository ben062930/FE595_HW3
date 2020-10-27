import pandas as pd
import nltk
from nltk import tokenize
from nltk.corpus import wordnet
import sys
sys.path.append("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/")
import wrap_business

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
    business_purpose = wrap_business.business_purpose
    get_tokens(business_purpose)