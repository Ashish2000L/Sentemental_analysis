from shortsent import sent
from sample import sentence
from matplotlib import  pyplot as plt
from matplotlib import style
import time
import pandas as pd
'''
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        
        print((tweet))

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
'''
def word():
    data=open('data.txt','r')
    for l in data:
        yield l
success=True
b=word()
dit={'shortsent':[],'update':[],'sample':[],'total_time':[]}
while success:
   try:
       initial=time.time()
       text=next(b)
       #text="corona is not dangerous, we don't have to worry about it!!"
       output,shortsent_time,update_time=sent(text)
       review,confidence,sample_time=sentence(output)
       final=time.time()-initial
       dit['shortsent'].append(shortsent_time)
       dit['update'].append(update_time)
       dit['sample'].append(sample_time)
       dit['total_time'].append(final)
   except:
       data_frame=pd.DataFrame(dit)
       data_frame.to_csv('testing.csv')
       success=False

style.use('ggplot')
df=pd.read_csv('testing.csv')
dct=dit
#print(df.head())
#print(dct)
dct=dct.rename(columns={'Unnamed: 0':'S_no'})
s_no=dct.get('S_no')
sen=dct.get('shortsent')
update=dct.get('update')
sample=dct.get('sample')
total_time=dct.get('total_time')
#print(total_time)
#print(sample)
plt.bar(s_no,[sen,update,sample,total_time],color='c')
plt.plot(s_no,update,"b",label='userdata',linewidth=0.5,kind='bar')
plt.plot(s_no,sample,"k",label='sentence',linewidth=0.5,kind='bar')
plt.plot(s_no,total_time,"r",label='Total_time',linewidth=0.5,kind='bar')
plt.title("Time taken on each inputs")
plt.ylabel('Time (sec)')
plt.xlabel('No. of inputs ')
plt.legend()
plt.show()
