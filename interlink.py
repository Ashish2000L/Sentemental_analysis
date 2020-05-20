import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sample import sentence
import nltk.text as txt
from statistics import mode
from shortsent import sent
from functools import reduce

# vecterizing the data
stops = set(stopwords.words('english'))
vect = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stops, ngram_range=(1, 3))

lst = []
lst_neg = []
global lt,lt_neg

def value(string1):
    global result
    string = str(string1)
    lt_neg = {}
    lt = {}
    try:
        file = open('neg.txt', 'rb')
        file_next = open('pos.txt', 'rb')

        try:
            for i in file:
                lst.append(i.decode())

            for z in file_next:
                lst_neg.append(z.decode())

            make_text_neg = txt.TextCollection(lst_neg)

            make_text = txt.TextCollection(lst)

            output = sent(string)
            print('passed: sent')

            result = sentence(output)
            print('passed: sentence')

            for i in output.split(' '):
                if i not in lt:
                    lt[i] = make_text.tf_idf(i, output)

            for j in output.split(' '):
                if j not in lt_neg:
                    lt_neg[j] = make_text_neg.tf_idf(j, output)

            print('passed: value')
        except AssertionError as ass:
            print(ass)

    except FileNotFoundError as fnf:
        print(fnf)
    else:
        return result, lt, lt_neg


def final_output(string):
    result, lt, lt_neg = value(string)
    print('passed: call->value')
    # to make visulization on each words

    pf_pos=[x[1] for x in lt.items()]
    pf_neg=[x[1] for x in lt_neg.items()]

    pos_mult = reduce(lambda x, y: x * y, list(filter(lambda a: (a != 0), pf_pos)))
    neg_mult = reduce(lambda x, y: x * y, list(filter(lambda a: (a != 0), pf_neg)))

    total = neg_mult + pos_mult

    pos_percnt =int( (pos_mult / total) * 100)
    neg_percnt =int( (neg_mult / total) * 100)

    # to handle error of mode
    try:
        print('entered in try block')
        res = mode(result)
        confidance = float((result.count(res) / len(result)) * 100)
        if res == 1:
            res = 'Positive'
        else:
            res = 'Negative'

        if confidance > 60:
            print('value returned')
            return res, confidance
        else:
            print(confidance)
            var=1
            return var,confidance

    except ArithmeticError as ar:
        print('entered in else block ')
        if pos_percnt > neg_percnt:
            result.append(1)
        else:
            result.append(0)
        res = mode(result)
        confidance = float((result.count(res) / len(result)) * 100)
        if res == 1:
            res = 'Positive'
        else:
            res = 'Negative'
        if confidance > 60:
            print('value returned')
            return res, confidance
        else:
            print(confidance)
            var=1
            return var, confidance
