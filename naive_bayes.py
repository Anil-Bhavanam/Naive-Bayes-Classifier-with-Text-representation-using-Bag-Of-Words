# -*- coding: utf-8 -*-
"""Naive bayes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16mLUldB_JfhMZZ4_o-zWhL6jgHjsc7Mu
"""

import pandas as pd
import numpy as np

dataframe=pd.read_csv("/content/spam.csv")
dataframe.head()

dataframe.Category.value_counts()

dataframe['spam']=dataframe.Category.apply(lambda x: 1 if x=="spam" else 0)

dataframe.head()

from numpy.random.mtrand import rand
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(dataframe.Message,dataframe.spam,test_size=0.2,random_state= 2)

print(f"train data size is {x_train.count()}")
print(f"test data size is {x_test.count()}")

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x_train_cv=cv.fit_transform(x_train)

x_train.shape

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x_train_cv,y_train)

x_test_cv=cv.transform(x_test)

y_pred=model.predict(x_test_cv)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

"""# **Will  implement in the sklearn pipeline**"""

from sklearn.pipeline import Pipeline
clf=Pipeline([('vectorizer',CountVectorizer()),('nb', MultinomialNB())])

clf.fit(x_train,y_train)

print(classification_report(y_test,clf.predict(x_test)))
