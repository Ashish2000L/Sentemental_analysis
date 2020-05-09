import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import  pyplot as plt
from matplotlib import style
from sample import sentence
import  nltk.text as txt
from statistics import mode
from shortsent import sent

#vecterizing the data
stops=set(stopwords.words('english'))
vect=TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii',stop_words=stops,ngram_range=(1,3))

lst=[]
lst_neg=[]

def value(string1):
    string=str(string1)
    lt_neg = {}
    lt = {}
    try:
        file=open('pos.txt', 'rb')
        file_next=open('neg.txt','rb')

        for i in file:
            lst.append(i.decode())

        for z in file_next:
            lst_neg.append(z.decode())

        make_text_neg=txt.TextCollection(lst_neg)

        make_text=txt.TextCollection(lst)

        output = sent(string)

        result=sentence(output)

        for i in output.split(' '):
            if i not in lt:
                lt[i]=make_text.tf_idf(i,output)

        for j in output.split(' '):
            if j not in lt_neg:
                lt_neg[j]=make_text_neg.tf_idf(j,output)
    except Exception as ec:
        print(ec)
    else:
        return result,lt,lt_neg
x=str(input("Enter your text: "))
result,lt,lt_neg=value(x)
file=open('testing_pos.csv','w')
file_neg=open('testing_neg.csv','w')
for z in lt:
    file.write(z)
    file.write(',')
    file.write(str(lt.get(z)))
    file.write('\n')

for k in lt_neg:
    file_neg.write(k)
    file_neg.write(',')
    file_neg.write(str(lt_neg.get(k)))
    file_neg.write('\n')
file.close()
file_neg.close()
pf_pos=pd.read_csv('testing_pos.csv', names=['words','tf_idf'])
pf_neg=pd.read_csv('testing_neg.csv',names=['words','tf_idf'])
#test = pf_pos.sort_values('tf_idf', ascending=False)#to short the values
initial=len(pf_pos['words'])
cf=pf_pos[pf_pos.tf_idf!=0.0]
#print('percentage matching: ',((len(cf['words'])/initial)*100))
pos_sum=sum(pf_pos['tf_idf'])
neg_sum=sum(pf_neg['tf_idf'])
total=neg_sum+pos_sum
pos_percnt=(pos_sum/total)*100
neg_percnt=(neg_sum/total)*100
try:
    res=mode(result)
    confidance = result.count(res) / len(result)
    if res == 1:
        res = 'Positive'
    else:
        res = 'Negative'
    print((res, confidance,len(result)))
except Exception as e:
    if pos_percnt>neg_percnt:
        result.append(1)
    else:
        result.append(0)
    res=mode(result)
    confidance = result.count(res) / len(result)
    if res == 1:
        res = 'Positive'
    else:
        res = 'Negative'
    print((res, confidance, len(result)))

