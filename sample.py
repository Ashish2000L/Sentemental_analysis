import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.corpus import stopwords
from statistics import mode
import numpy as np
import time

start=time.time()

#get the detailed data
dp1=pd.read_csv('positive.txt', sep='\t', names=['likes', 'text'])
dp2=pd.read_csv('negative.txt', sep='\t', names=['likes', 'text'])

concat=pd.concat([dp1,dp2])

Y=concat.likes
#vecterizing the data
stops=set(stopwords.words('english'))
vect=TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii',stop_words=stops)
X=vect.fit_transform(concat.text)

#spliting the data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=5)

#training using MultinomialNB
clf=naive_bayes.MultinomialNB()
clf.fit(X_train,Y_train)

#to check the accuracy of the process
from sklearn.naive_bayes import GaussianNB

#gnb=GaussianNB()
clf=MultinomialNB()
BNB_classifier=BernoulliNB()
LR_classifier=LogisticRegression()
SGDC_classifier=SGDClassifier()
SVC_classifier=SVC()
LSVC_classifier=LinearSVC()
NSVC_classifier=NuSVC()



#this is how we find accuracy
'''gnb.fit(X_train.toarray(),Y_train)
Y_pred_gnb=gnb.predict(X_test.toarray())
print("Accuracy of GaussianNB: ",metrics.accuracy_score(Y_test,Y_pred_gnb)*100)'''

clf.fit(X_train.toarray(),Y_train)

BNB_classifier.fit(X_train.toarray(),Y_train)

LR_classifier.fit(X_train.toarray(),Y_train)

SGDC_classifier.fit(X_train.toarray(),Y_train)

LSVC_classifier.fit(X_train.toarray(),Y_train)

#function to pass the string
votes=[]
def sentence(sent):
    movie_review_vect=vect.transform(np.array([sent]))
    review = clf.predict(movie_review_vect)
    votes.append(review)
    review = BNB_classifier.predict(movie_review_vect)
    votes.append(review)
    review = LR_classifier.predict(movie_review_vect)
    votes.append(review)
    review = SGDClassifier.predict(LSVC_classifier,movie_review_vect)
    votes.append(review)
    review = LSVC_classifier.predict(movie_review_vect)
    votes.append(review)
    list = []
    for i in votes:
        list.append(i[0])
    res = mode(list)
    num = list.count(res)
    conf = num / len(list)
    if res == 1:
        res = 'Positive'
    elif res == 0:
        res = 'Negative'
    return res, conf*100
print('Time taken to interpret: ',time.time()-start)
