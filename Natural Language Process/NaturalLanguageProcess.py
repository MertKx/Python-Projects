# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:03:13 2024

@author: mertk
""",

# we will classify male and female users from tweets
import pandas as pd


#%% import twitter data

data = pd.read_csv(r"gender_classifier.csv",encoding="latin1")
# r=read encoding latin = latin alphabet

data = pd.concat([data.gender,data.description],axis=1)
data.dropna(axis=0,inplace=True)
#female 1 male 0
data.gender = [1 if each == "female" else 0 for each in data.gender]

#%% cleaning data
#regular expression RE ex="[^a-zA-Z]"

import re

first_description = data.description[4]
description = re.sub("[^a-zA-Z]"," ",first_description) 
#a dan z ye ve A dan Z ye kadar olan harfleri alma geri kalani 
#" " bosluk ile degistir 
description = description.lower() #lower case the letters

#%% stopwords (irrelavent words)

import nltk 
nltk.download("stopwords") #corpus adli klasore iniyor
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords #corpustan import ediyoruz

#description = description.split()

#we can use tokenizer instead of split
description = nltk.word_tokenize(description)

# split kullanirsak shouldn't gibi kelimelerdeki not kismi ayrilmaz
#%% 
#gereksiz kelimeleri cikariyoruz

description = [word for word in description if not word in set(stopwords.words("english"))]
#%%
#lemmatazation loves=>love

import nltk as nlp

lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description]

description = " ".join(description)
#%%

for description in data.description:
    description = re.sub("[^a-zA-Z]"," ",description) 
    description = description.lower()
    description = nltk.word_tokenize(description)
    description = [word for word in description if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    description = [lemma.lemmatize(word) for word in description]
    description = " ".join(description)
    description_list.append(description)
    
#%% bag of words

from sklearn.feature_extraction.text import CountVectorizer # bag of words yaratmak icin kullandigim metot
max_features = 5000

count_vectorizer = CountVectorizer(max_features=max_features,stop_words = "english")

sparce_matrix = count_vectorizer.fit_transform(description_list).toarray()  # x

print("en sik kullanilan {} kelimeler: {}".format(max_features,count_vectorizer.get_feature_names()))

# %%
y = data.iloc[:,0].values   # male or female classes
x = sparce_matrix
# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1, random_state = 42)


# %% naive bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train,y_train)

#%% prediction
y_pred = nb.predict(x_test)

print("accuracy: ",nb.score(y_pred.reshape(-1,1),y_test))













