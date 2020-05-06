import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import  pyplot as plt
from matplotlib import style
from sample import sentence
import  nltk.text as txt
from statistics import mode
from shortsent import sent

#def word():
#    data=open('data.csv','r')
#    for l in data:
#        yield l
#success=True
#b=word()
#dit={'shortsent':[],'update':[],'sample':[],'total_time':[]}
#while success:
#   try:
#       initial=time.time()
#       text=next(b)
#       #text="corona is not dangerous, we don't have to worry about it!!"
#       output,shortsent_time,update_time=sent(text)
#       review,confidence,sample_time=sentence(output)
#       final=time.time()-initial
#       dit['shortsent'].append(shortsent_time)
#       dit['update'].append(update_time)
#       dit['sample'].append(sample_time)
#       dit['total_time'].append(final)
#   except:
#       data_frame=pd.DataFrame(dit)
#       data_frame.to_csv('testing.csv')
#       success=False
#
#style.use('ggplot')
#df=pd.read_csv('testing.csv')
#dct=dit
##print(df.head())
##print(dct)
#dct=dct.rename(columns={'Unnamed: 0':'S_no'})
#s_no=dct.get('S_no')
#sen=dct.get('shortsent')
#update=dct.get('update')
#sample=dct.get('sample')
#total_time=dct.get('total_time')
##print(total_time)
##print(sample)
#plt.bar(s_no,[sen,update,sample,total_time],color='c')
#plt.plot(s_no,update,"b",label='userdata',linewidth=0.5,kind='bar')
#plt.plot(s_no,sample,"k",label='sentence',linewidth=0.5,kind='bar')
#plt.plot(s_no,total_time,"r",label='Total_time',linewidth=0.5,kind='bar')
#plt.title("Time taken on each inputs")
#plt.ylabel('Time (sec)')
#plt.xlabel('No. of inputs ')
#plt.legend()
#plt.show()

dp1=pd.read_csv('pos.csv',names=['Rev','Text'])
dp2=pd.read_csv('neg.csv', names=['Rev','Text'])

concat=pd.concat([dp1,dp2])

Y=concat.Rev

#vecterizing the data
stops=set(stopwords.words('english'))
vect=TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii',stop_words=stops,ngram_range=(1,3))

#X=vect.fit_transform(concat.Text)


lst=[]
lst_neg=[]
lt_neg={}
lt={}
def value(string1):
    string=str(string1)
    try:
        file=open('pos.txt', 'rb')
        file_next=open('neg.txt','rb')
        for i in file:
            lst.append(i.decode())

        for z in file_next:
            lst_neg.append(z.decode())
        make_text_neg=txt.TextCollection(lst_neg)
        make_text=txt.TextCollection(lst)
        output, shortsent_time, update_time = sent(string)
        print(output)
        result,confi=sentence(output)
        for i in output.split(' '):
            if i not in lt:
                lt[i]=make_text.tf_idf(i,output)

        for j in output.split(' '):
            if j not in lt_neg:
                lt_neg[j]=make_text_neg.tf_idf(j,output)
    except Exception as ec:
        print('hello')
        print(ec)
    else:
        return result,confi
x=str(input("Enter your text: "))
result,confi=value(x)
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
    file_neg.write(str(lt.get(k)))
    file_neg.write('\n')
file.close()
file_neg.close()
#items=[x[1] for x in lt.items()]
#style.use('ggplot')
#plt.plot(list(lt.keys()),items,'r',linewidth=1)
#plt.title(f"Tf-idf of string:\n{x}")
#plt.ylabel('tf_idf value')
#plt.xlabel('words ')
##plt.legend()
#plt.show()
#print((result,confi))
pf_pos=pd.read_csv('testing_pos.csv', names=['words','tf_idf'])
pf_neg=pd.read_csv('testing_neg.csv',names=['words','tf_idf'])
#test = pf_pos.sort_values('tf_idf', ascending=False)#to short the values
initial=len(pf_pos['words'])
cf=pf_pos[pf_pos.tf_idf!=0.0]
print('percentage matching: ',((len(cf['words'])/initial)*100))
pos_sum=sum(pf_pos['tf_idf'])
neg_sum=sum(pf_neg['tf_idf'])
if pos_sum > neg_sum:
    print('Matching to the positive: ',pos_sum)
    result.append(1)
else:
    print('Matching to the negative: ',neg_sum)
    result.append(0)

res=mode(result)
confidance=result.count(res)/len(result)
if res==1:
    res='Positive'
else:
    res='Negative'

print((res,confidance))
