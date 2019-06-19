#!/usr/bin/env python3
# coding: utf-8

import re						
import nltk						
#jhhgfjhfasdfghgjhg
regex = re.compile(r'(\w+)?( )?(-{4})( )?(\w+)')	
nregex = re.compile(r'(-{4})')
list_ans = input()
paragraph=input()
list_ans = []
for line in paragraph.split('.'):
   
    robject = regex.search(line)
    if (robject == None):				 
        continue
    contex = nltk.word_tokenize(line)
    contex = nltk.pos_tag(contex)			
    for p in contex:
        if(p[1] in ('VBD' , 'VBN')):			
            past = True
            break
        else:past = False
    for subline in line.split(','):
        robject = regex.search(subline)
        if (robject == None):
            continue            
        if(nltk.pos_tag([robject.group(1)])[0][1] in ('NNS' , 'NNPS')):	
            plural = True
        else: plural = False
        if(nltk.pos_tag([robject.group(5)])[0][1] in ('VBD' ,'VBN')):
            object_word_past = True
        else:object_word_past = False
        if(nltk.pos_tag([robject.group(1)]) in ('PRP' , 'VBN')):		
            pronoun = True
        else:pronoun = False
            
        if(past):
                if(plural):
                    nregex.sub('were',subline)					
                    list_ans.append('were')					
                    continue
                elif(not plural and not pronoun):
                    list_ans.append('was')
                    continue
                elif(pronoun and robject.group(1) == 'I'):
                    list_ans.append('was')
                    continue
                elif(pronoun and robject.group(1) in ('We','You','They')):
                    list_ans.append('were')
                    continue
                elif(robject.group(1) in ('have' , 'had' )):
                    list_ans.append('been')
                    continue
                elif(nltk.pos_tag([robject.group(5)])[0][1] in ('VBD' ,'VBN')):
                    list_ans.append('was')
                    
                
        if(robject.group(1) == 'I'):
            list_ans.append('am')
            continue
        elif(robject.group(1) in ('You','We','They')):
            list_ans.append('are')
            continue
        elif(nltk.pos_tag([robject.group(1)])[0][1] == 'NN'):
            list_ans.append('is')
            continue
        elif(robject.group(1) in ('He','She','It')):
            list_ans.append('is')
            continue
        elif(robject.group(1) == 'will'):
            list_ans.append('be')
            continue
        
for ans in list_ans:
    print(ans)




