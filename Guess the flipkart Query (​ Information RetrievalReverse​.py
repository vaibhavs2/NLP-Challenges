#!/usr/bin/env python
# coding: utf-8

from fuzzywuzzy import process
import pandas as pd
column=['product','catagory']
try:
    data = pd.read_csv('/home/next/Desktop/training.txt', sep=r'\t',header = None,names=column)
    catagory=[r for r in data['catagory'].unique()]
except FileNotFoundError:
        print("training file doesn't exists")
product=input()

for i in range(0,len(product),60):
    chunk=product[i:i+60]
    print(process.extractOne(chunk, catagory)[0])
