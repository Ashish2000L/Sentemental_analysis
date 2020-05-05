from shortsent import sent
from sample import sentence
from matplotlib import  pyplot as plt
from matplotlib import style
import nltk.text as txt
import time
import pandas as pd

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

lst=[]
lt={}
def value(string):
    try:
        file=open('C:\\Users\\pratibha\\PycharmProjects\\test\\positive.txt','r')
        for i in file:
            lst.append(i)
        make_text=txt.TextCollection(lst)
        output, shortsent_time, update_time = sent(string)

        for i in output.split(' '):
            if i not in lt:
                lt[i]=make_text.tf_idf(i,output)
    except Exception as ec:
        print(ec)
    else:
        return lt,string

val,user_string=value(str(input("Enter your text: ")))
file=open('testing.csv','w')
for z in lt:
    file.write(z)
    file.write(',')
    file.write(str(val.get(z)))
    file.write('\n')
file.close()
items=[x[1] for x in lt.items()]
style.use('ggplot')
plt.plot(list(lt.keys()),items,'r',linewidth=1)
plt.title(f"Tf-idf of string:\n{user_string}")
plt.ylabel('tf_idf value')
plt.xlabel('words ')
#plt.legend()
plt.show()