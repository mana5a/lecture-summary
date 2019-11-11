import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import re
stop_words = set(stopwords.words('english'))

def generate(res):
    #file=pd.read_csv('./files/text.txt')
    

    #valid=file
    #lines=valid
    #print(lines)
    # sent=[]
    # words=[]
    # for line in lines:
    #     sent.extend(nltk.sent_tokenize(line.lower()))
    # for sen in sent:
    #     words.extend(nltk.word_tokenize(sen))
    # tokens=[x for x in words if x.isalpha()]
    #print(tokens)

    # file=open('./files/text.txt','r')
    data1=res
    # file.close()
    print(data1)
    data=data1[0].lower()

    phrases = sent_tokenize(data)
    words = word_tokenize(data)

    print(phrases)
    print(len(phrases))
    sent=phrases
    print(words)

    tokens=[x for x in words if x.isalpha()]

    final=[]
    for word in tokens:
        if word not in stop_words:
            final.append(word)
    
    token_fd = nltk.FreqDist(final)
    keywords=token_fd.most_common(10)

    mod_sen=[]
    for sen in sent:
        score=0
        keys=[]
        for word in nltk.word_tokenize(sen):
            score+=token_fd[word]   
            if token_fd[word]>2:
                keys.append(word) 
        mod_sen.append((sen,score,list(set(keys))))
    #print(mod_sen)

    sort_final=sorted(mod_sen,key=lambda tup: tup[1])

    a=[]
    for i in sort_final[len(sort_final)-5:]:
        a.append((i[0],i[2],i[1])) #sending only sentence and the keywords
        a.reverse()
        print(a) 
    
    return (a,keywords,data1)