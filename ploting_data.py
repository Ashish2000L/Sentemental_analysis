from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

#for scattering view
def tsne_plot(model,set_lst):
    labels = []
    wordvecs = []

    for word in set_lst:
        wordvecs.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=3, n_components=2, init='pca', random_state=42)
    coordinates = tsne_model.fit_transform(wordvecs)

    x = []
    y = []
    for value in coordinates:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(8, 8))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(2, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

#plotting bar graph
def plotting(file_name):
    df=pd.read_csv(file_name)

    df.set_index('main',inplace=True)
    df.head(10)
    df.plot(kind='bar')
    plt.show()

#ploting multiple graphs
def plots():
    df=pd.read_csv('fuzywuzy_data.csv')
    lf1=df.get(['ratio'])
    lf2=df.get(['partial_ratio'])
    lf3=df.get(['token_sort_ratio'])
    lf4=df.get('token_set_ratio')
    lf1.plot(kind='hist')
    plt.show()
    lf2.plot(kind='hist')
    plt.show()
    lf3.plot(kind='hist')
    plt.show()
    lf4.plot(kind='hist')
    plt.show()