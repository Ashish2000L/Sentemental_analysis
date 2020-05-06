import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes, metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
from nltk.corpus import stopwords
from statistics import mode
import pickle
import numpy as np
import time


#get the detailed data
dp1=pd.read_csv('pos.csv',names=['Rev','Text'])
dp2=pd.read_csv('neg.csv',names=['Rev','Text'])

concat=pd.concat([dp1,dp2])

Y=concat.Rev

#vecterizing the data
stops=set(stopwords.words('english'))
vect=TfidfVectorizer(use_idf=True,lowercase=True, strip_accents='ascii',stop_words=stops,ngram_range=(1,3),)

X=vect.fit_transform(concat.Text)

#spliting the data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=5)

#training using MultinomialNB
gnb=GaussianNB()
MNB_classifier=MultinomialNB()
BNB_classifier=BernoulliNB()
LR_classifier=LogisticRegression()
SGDC_classifier=SGDClassifier()
LSVC_classifier=LinearSVC()


#this is how we find accuracy
gnb.fit(X_train.toarray(),Y_train)
Y_pred_gnb=gnb.predict(X_test.toarray())
#print("Accuracy of GaussianNB: ",metrics.accuracy_score(Y_test,Y_pred_gnb)*100)

MNB_classifier.fit(X_train.toarray(),Y_train)
Y_pred_MNB=MNB_classifier.predict(X_test.toarray())
#print("Accuracy of MNB_classifier: ",metrics.accuracy_score(Y_test,Y_pred_MNB)*100)

#pickled and loaded the MNB_classifier
multinomial_classifier=open('multinom_clf.pickle','wb')
pickle.dump(MultinomialNB,multinomial_classifier)
multinomial_classifier.close()

BNB_classifier.fit(X_train.toarray(),Y_train)
Y_pred_BNB=BNB_classifier.predict(X_test.toarray())
#print("Accuracy of BNB_classifier: ",metrics.accuracy_score(Y_test,Y_pred_BNB)*100)

#pickled and loaded the BNB_classifier
Bernauli_classifier=open('bernauli_clf.pickle','wb')
pickle.dump(BNB_classifier,Bernauli_classifier)
Bernauli_classifier.close()

LR_classifier.fit(X_train.toarray(),Y_train)
Y_pred_LR=LR_classifier.predict(X_test.toarray())
#print("Accuracy of LR_classifier: ",metrics.accuracy_score(Y_test,Y_pred_LR)*100)

#pickled and loaded the LR_classifier
logistic_classifier=open('logistic_clf.pickle','wb')
pickle.dump(LR_classifier,logistic_classifier)
logistic_classifier.close()

SGDC_classifier.fit(X_train.toarray(),Y_train)
Y_pred_SGDC=SGDC_classifier.predict(X_test.toarray())
#print("Accuracy of SGDC_classifier: ",metrics.accuracy_score(Y_test,Y_pred_SGDC)*100)

#pickled and loaded the SGDC_classifier
sgdc_classifier=open('SGDC_clf.pickle','wb')
pickle.dump(SGDC_classifier,sgdc_classifier)
sgdc_classifier.close()

LSVC_classifier.fit(X_train.toarray(),Y_train)
Y_pred_LSVC=LSVC_classifier.predict(X_test.toarray())
#print("Accuracy of LSVC_classifier: ",metrics.accuracy_score(Y_test,Y_pred_LSVC)*100)

#pickled and loaded the LSVC_classifier
lsvc_classifier=open('LSVC_clf.pickle','wb')
pickle.dump(LSVC_classifier,lsvc_classifier)
lsvc_classifier.close()

NuSVC_classifier=NuSVC()
NuSVC_classifier.fit(X_train.toarray(),Y_train)
Y_pred_NuSVC=NuSVC_classifier.predict(X_test.toarray())
#print("Accuracy of NuSVC_classifier: ",metrics.accuracy_score(Y_test,Y_pred_NuSVC)*100)

#pickled nusvc_classifier
nusvc_classifier=open('NuSVC_clf.pickle','wb')
pickle.dump(NuSVC_classifier,nusvc_classifier)
nusvc_classifier.close()

SVC_classifier=SVC()
SVC_classifier.fit(X_train.toarray(),Y_train)
Y_pred_SVC=SVC_classifier.predict(X_test.toarray())
#print("Accuracy of SVC_classifier: ",metrics.accuracy_score(Y_test,Y_pred_SVC)*100)

#pickled svc_classifier
svc_classifier=open('svc_clf.pickle','wb')
pickle.dump(SVC_classifier,svc_classifier)
svc_classifier.close()

#function to pass the string
votes=[]
def sentence(sent):
    sample_start = time.time()
    vectors=vect.transform(np.array([sent]))#np.array([sent])
    review=gnb.predict(vectors.toarray())
    votes.append(review)
    review=SVC_classifier.predict(vectors.toarray())
    votes.append(review)
    review=NuSVC_classifier.predict(vectors.toarray())
    votes.append(review)
    review = MNB_classifier.predict(vectors.toarray())
    votes.append(review)
    review = BNB_classifier.predict(vectors.toarray())
    votes.append(review)
    review = LR_classifier.predict(vectors.toarray())
    votes.append(review)
    review = SGDC_classifier.predict(vectors.toarray())
    votes.append(review)
    review = LSVC_classifier.predict(vectors.toarray())
    votes.append(review)
    list = []
    for i in votes:
        list.append(i[0])
    #res = mode(list)
    #num = list.count(res)
    #conf = num / len(list)
    #if res == 1:
    #    res = 'Positive'
    #elif res == 0:
    #    res = 'Negative'
    #sample_time = time.time() - sample_start
    return list
