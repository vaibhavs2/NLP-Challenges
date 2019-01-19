#!/usr/bin/env python
# coding: utf-8

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
column = ['product','category']
data = pd.read_csv('/home/next/Desktop/training.txt',sep='\t',names=column) #addressing to training file in system
vector = CountVectorizer()
vector.fit(data['product'][1:])
counts = vector.transform(data['product'][1:])
mn= MultinomialNB()
mn.fit(counts,data['category'][1:])
print('Enter number of queries line')
number_of_lines=int(input())
lines=[]
print('paste queries')
for i in range(number_of_lines):    
    query=input()
    lines.append(query)

line=mn.predict(vector.transform(lines))

for ansr in line:
        print(ansr)
    
