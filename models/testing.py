# -*- coding: utf-8 -*-
"""TESTING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X1hneOvCFnCxxUwiZUU0r4WH96X2jAoI
"""

#import libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.pipeline import Pipeline
import pickle
from sklearn.externals import joblib

#data preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn import *

#NLP tools
import re
import nltk
nltk.download('stopwords')
nltk.download('rslp')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

#train split and fit models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from nltk.tokenize import TweetTokenizer

#model selection
from sklearn.metrics import confusion_matrix, accuracy_score, plot_confusion_matrix, classification_report
import os
import pickle

#Preprocessing 
def preprocessing(data):
    stemmer = nltk.stem.RSLPStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    corpus = []
    for words in data:
      review = re.sub(r"@[A-Za-z0-9_]+", " ", words)
      review = re.sub('RT', ' ', review)
      review = re.sub(r"https?://[A-Za-z0-9./]+", " ", review)
      review = re.sub(r"https?", " ", review)
      review = re.sub('[^a-zA-Z]', ' ', review)
      review = review.lower()
      review = review.split()
      ps = PorterStemmer()
      review = [ps.stem(word) for word in review if not word in set(all_stopwords) if len(word) > 2]
      review = ' '.join(review)
      corpus.append(review)

    return np.array(corpus)

path_to_data = '/content/drive/MyDrive/ISFCR Project folder/labeled_data.csv'
PATH_TO_NLTK_MODEL = '/content/drive/MyDrive/ISFCR Project folder/nltk.pickle'
PATH_TO_SCIKIT_MODEL = '/content/drive/MyDrive/ISFCR Project folder/model.pkl'

classifier_f = open(PATH_TO_NLTK_MODEL, "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

m = joblib.load(PATH_TO_SCIKIT_MODEL)

def testing(data, vectorizer, model):
    tweet_tokenizer_test = TweetTokenizer() 
    arr = list([data,])
    arr = preprocessing(arr)
    check = vectorizer.transform(arr)
    return model.predict(check)

print(testing('yeah great one actual fuck hilari bitch', classifier, m))
print(testing('this is a good cake', classifier, m))
print(testing('I swear i do not support the usage of this word but, nigger', classifier, m))
#class 0 - hate speech
#class 1- offensive
#class 2- not offensive/ hateful
