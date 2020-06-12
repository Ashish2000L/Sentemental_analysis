#import cv2
#import numpy
#import pytesseract
#from PIL import Image
from interlink import final_output
from fuzywuzy import str_cmp
from bs4 import BeautifulSoup
from statistics import mode
import requests
global text
print("Choose the way you want to input the news: ")
x = input("I for image and T for text: ")
if x.upper() == "T":
    text = input("Enter news that you want to search: ")
    #print(text)
elif x.upper() == "I":
    image_input = input('Enter detail related to image: ')
    print(image_input)
    #img = cv2.imread(image_input)
    #text = pytesseract.image_to_string(img)
    print("\n")
    #print(text)
else:
    print("Invalid input")
    quit(0)
import nltk
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
#print(words)
main_text = ' '.join(map(str, words))
#print(main_text)

import urllib.request
files = open('url_texts.txt', 'w')
def connect(host = 'https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

count=0
lst=[]
file = open("url_data.csv", 'wb')
if connect():
    from googlesearch import search
    query = text    #co.in
    for url in search(query, tld='com', lang='en', start=0, pause=1.0):
        try:
            #print("\n")
            #print("\n")
            URL = url
            content = requests.get(URL)
            soup = BeautifulSoup(content.text, 'html.parser')
            ext_text = soup.find_all('p', limit=8)

            #for para in ext_text:
            #    i = para.get_text()
            #    i = i.replace(',', '')
            #    i = i.replace('”', '')
            #    i = i.replace('“', '')
            #    i = i.replace('’', '')
            #    i=i.replace('–',' ')
            #    i = i.replace('‘', '')
            #    i = i.replace('’', '')
            #    file.write(i)
            #    files.write(i)
            #    files.write('\n')
            #    file.write(b'\n')

            ##file.close()
            #files.write('\n')
            #str_cmp(text)
            from newspaper import Article
            from newspaper import Config

            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            config=Config()
            config.browser_user_agent=user_agent
            # For different language newspaper refer above table
            article = Article(url, language="en",config=config)  # en for English

            # To download the article
            article.download()

            # To parse the article
            article.parse()

            # To perform natural language processing ie..nlp
            article.nlp()

            i = article.summary
            i = i.replace(',', '')
            i = i.replace('”', '')
            i = i.replace('“', '')
            i = i.replace('’', '')
            i = i.replace('–', ' ')
            i = i.replace('‘', '')
            i = i.replace('’', '')
            i = i.replace("'", '')
            i = i.replace('"', '')
            #try:
            result, confidance = final_output(i)
            if result=='Positive':
                print(url)
                print("Final result: ", result, confidance)
                count+=1
                lst.append(1)
            elif result == 'Negative':
                print(url)
                print("Final result: ", result, confidance)
                count+=1
                lst.append(0)

            file.write(i.encode())
            file.write(b'\n')
            #count+=1
            if(count==23):
                break
        except Exception as ex:
            continue
else:
    print("not connected")
file.close()
finl_relult=mode(lst)
if finl_relult==1:
    print("\n\n\t\t",'Positive')
elif finl_relult==0:
    print('\n\n\t\t','Negative')
else:
    print('\n\n\t\t Cannot predict')

x=str_cmp(text)
files.close()