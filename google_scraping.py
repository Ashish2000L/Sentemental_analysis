#import cv2
import numpy
#import pytesseract
#from PIL import Image
from interlink import final_output
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
def connect(host = 'https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


if connect():
    from googlesearch import search
    query = text
    for url in search(query, tld='co.in', lang='en', num=10, start=0, stop= 5, pause=2.0):
        print("\n")
        print(url)
        print("\n")
        from newspaper import Article

        # For different language newspaper refer above table
        article = Article(url, language="en")  # en for English

        # To download the article
        article.download()

        # To parse the article
        article.parse()

        # To perform natural language processing ie..nlp
        article.nlp()

        # To extract title
        #print("News Title:")
        #print(article.title)
        #print("\n")
        # To extract complete Text of news
        #print("News Text:")
        #print(article.text)
        #print("\n")
        # To extract Summary of news
        #print("News Summary:")
        #print(article.summary)
        #print("\n")

        # To extract keywords of news
        #print("News Keywords:")
        #print(article.keywords)
        inpt = article.title
        print(inpt)
        try:
            result, confidance = final_output(inpt)
            print("Final result: ",result, confidance)
        except Exception as ec:
            print("\n Unable to find result, please try again later :) ")


else:
    print("not connected")