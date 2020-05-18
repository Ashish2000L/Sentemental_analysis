from shortsent import sent
from nltk.corpus import stopwords
import nltk
from gensim.models import Word2Vec
from scipy.stats import cosine
#from scipy.spatial.distance import cosine
import gensim.downloader as api
import re

inpt = input("Enter your text: ")
output = sent(inpt)
file = open('new_file.txt', 'r')
paragraph = file.read()
text = re.sub(r'\[[0-9]"\]', ' ', paragraph)
text = re.sub(r"\s+", ' ', text)
text = text.lower()
text = re.sub(r'\s+', ' ', text)

user_text = nltk.word_tokenize(output)

sentence = nltk.sent_tokenize(text)
sentence = [nltk.word_tokenize(x) for x in sentence]

for i in range(len(sentence)):
    sentence[i] = [word for word in sentence[i] if word not in stopwords.words('english')]

model = Word2Vec(sentence, min_count=1, size=100, window=5, sg=1)

words = model.wv.vocab

vector_corona = model.wv['corona']

vector_covid = model.wv['coronavirus']

similar = model.wv.most_similar('corona')

sim = model.wv.similarity('corona', 'coronavirus')

glove_model = api.load('glove-wiki-gigaword-300')
overall = []
file = open('neg.txt', 'r')
x = file.readline()
line = nltk.word_tokenize(sent(x))
output=[]
# for f in line:
for j in user_text:
    lst=[]
    for i in line:
        try:
            # using glove
            # print(f"\n\n{i} using glove: \n",glove_model[i])
            k = glove_model[i]
            m = glove_model[j]
            lst.append(cosine(m,k))
        except:
            try:
                # using word2vec
                # print(f"\n\n{i} using word2vec: \n",model.wv[i])
                k = model.wv[i]
                m = model.wv[j]
                lst.append([cosine(m,k)])
            except:
                print(f"\n\n {i}no text exist!! \n")
                lst.append([float(1)])
    output.append(lst)

print("\n\n Users text: \n", user_text)
print("\n\n Doc text: \n", line)
for i in output:
    print(i)
    print('\r')
