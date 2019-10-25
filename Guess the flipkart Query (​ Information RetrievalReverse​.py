from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import nltk
column = ['product','category']
data = pd.read_csv('/home/next/Desktop/training.txt',sep='\t',names=column)
vector = CountVectorizer()
vector.fit(data['product'][1:])
counts = vector.transform(data['product'][1:])
mn= MultinomialNB()
mn.fit(counts,data['category'][1:])
print('Enter number of queries line')
number_of_lines=int(input())
result=[]
print('paste queries')
for i in range(number_of_lines):    
    query=input()
    l=[]
    extract_nouns = word_tokenize(query)
    extract_nouns = nltk.pos_tag(extract_nouns)
    for each in extract_nouns:
        if(each[1] in ('NN','NNS','NNP','NNPS','SYM')):    
            l.append(each[0])
        else:
                continue
    query=' '.join(l)
    result.append(query)


for ansr in mn.predict(vector.transform(result)):
        print(ansr)
    
