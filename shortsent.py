#In this file we have we just make short sentence
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
lema=WordNetLemmatizer()

words_required=['not','neither','never','nope','do','can','will','shall']
stop_words=[i for i in stopwords.words('english') if i not in words_required ]

def eng_connections(list):
    ex_words={"'m":'am',"n't":'not',"'d":'had',"'s":'is',"'ll":'will',"'ve":'have',"'re":'are'}
    main_words={'sha':'shall','wo':'will','ca':'can'}
    key=main_words.keys()
    items=ex_words.keys()
    z=list
    for i in range(len(z)):
        if (z[i] in key):
            back=ex_words.get(z[i+1])
            front=main_words.get(z[i])
            z.pop(i+1)
            z.insert(i+1,back)
            z.pop(i)
            z.insert(i,front)
        elif z[i] in items:
            back=ex_words.get(z[i])
            z.pop(i)
            z.insert(i,back)
    return z

def sent(string):
    dict={'N':wn.NOUN,'J':wn.ADJ,'R':wn.ADV,'V':wn.VERB}
    req_pos_tags=['N','J','R','V']
    tokeniz=word_tokenize(string) #to tokenize words
    newlst=eng_connections(tokeniz) #handle words like don't, won't, counldn't etc.
    print(newlst)
    sit=[x.lower() for x in newlst] #all words in lowercase
    symb="!|\#$%^&*()+=-_~`<>.,?/:;{}[]"
    sym=[i for i in sit if i not in list(symb)] #Removed symbols
    stop=[i for i in sym if i not in stop_words] #removed stopwords
    tokens=nltk.pos_tag(stop) #added pos to list
    lst=[lema.lemmatize(i[0],dict.get(i[1][0])) for i in tokens if i[1][0] in req_pos_tags] #lemmatized list
    str=''
    for i in lst:
        str=str+' '+i  #to make list to string
    str=str.lstrip(" ") #removed extra spaces
    return str