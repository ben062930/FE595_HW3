from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
sys.path.append("/Users/jiefudong/Desktop/Jeff/SIT/FA/FE595/HW3/")
import wrap_business

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
    business_purpose = wrap_business.business_purpose
    score(business_purpose)
