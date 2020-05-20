import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes, metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
from nltk.corpus import stopwords
import pickle
import numpy as np

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

#gnb=GaussianNB()
#MNB_classifier=MultinomialNB()
#BNB_classifier=BernoulliNB()
#LR_classifier=LogisticRegression()
#SGDC_classifier=SGDClassifier()
#LSVC_classifier=LinearSVC()
#NuSVC_classifier=NuSVC()
#SVC_classifier=SVC()

#load Gaussian classifier
gaussain_classifier=open('gaussian_clf.pickle','rb')
gnb=pickle.load(gaussain_classifier)
gaussain_classifier.close()

#gnb.fit(X_train.toarray(),Y_train)
#gaussain_classifier=open('gaussian_clf.pickle','wb')
#pickle.dump(gnb,gaussain_classifier)
#gaussain_classifier.close()


#load multinomial pickle
multinomial_classifier=open('multinom_clf.pickle','rb')
MNB_classifier=pickle.load(multinomial_classifier)
multinomial_classifier.close()

#MNB_classifier.fit(X_train.toarray(),Y_train)
#multinomial_classifier=open('multinom_clf.pickle','wb')
#pickle.dump(MNB_classifier,multinomial_classifier)
#multinomial_classifier.close()

#load bernauli pickle
bernauli_classifier=open("bernauli_clf.pickle",'rb')
BNB_classifier=pickle.load(bernauli_classifier)
bernauli_classifier.close()

#BNB_classifier.fit(X_train.toarray(),Y_train)
#bernauli_classifier=open('bernauli_clf.pickle','wb')
#pickle.dump(BNB_classifier,bernauli_classifier)
#bernauli_classifier.close()

#load logical regression classifier
lr_classifier=open('logistic_clf.pickle','rb')
LR_classifier=pickle.load(lr_classifier)
lr_classifier.close()

#LR_classifier.fit(X_train.toarray(),Y_train)
#lr_classifier=open('logistic_clf.pickle','wb')
#pickle.dump(LR_classifier,lr_classifier)
#lr_classifier.close()

#load sgvc classifier
svgc_classifier=open('SGDC_clf.pickle','rb')
SGDC_classifier=pickle.load(svgc_classifier)
svgc_classifier.close()

#SGDC_classifier.fit(X_train.toarray(),Y_train)
#svgc_classifier=open('SGDC_clf.pickle','wb')
#pickle.dump(SGDC_classifier,svgc_classifier)
#svgc_classifier.close()

#load lsvc classifier
lsvc_classifier=open('LSVC_clf.pickle','rb')
LSVC_classifier=pickle.load(lsvc_classifier)
lsvc_classifier.close()

#LSVC_classifier.fit(X_train.toarray(),Y_train)
#lsvc_classifier=open('LSVC_clf.pickle','wb')
#pickle.dump(LSVC_classifier,lsvc_classifier)
#lsvc_classifier.close()

#load svc classifier
nusvc_classifier=open('NuSVC_clf.pickle','rb')
NuSVC_classifier=pickle.load(nusvc_classifier)
nusvc_classifier.close()

#NuSVC_classifier.fit(X_train.toarray(),Y_train)
#nusvc_classifier=open('NuSVC_clf.pickle','wb')
#pickle.dump(NuSVC_classifier,nusvc_classifier)
#nusvc_classifier.close()

#load svc classifier
svc_classifier=open('svc_clf.pickle','rb')
SVC_classifier=pickle.load(svc_classifier)
svc_classifier.close()

#SVC_classifier.fit(X_train.toarray(),Y_train)
#svc_classifier=open('svc_clf.pickle','wb')
#pickle.dump(SVC_classifier,svc_classifier)
#svc_classifier.close()

#function to pass the string

def sentence(sent):
    votes = []
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
    print('\n',list)
    return list