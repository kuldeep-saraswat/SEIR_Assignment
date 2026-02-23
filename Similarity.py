import sys
import requests

def simhash_compare(u1,u2):

    def simple_hash(word):
        p=53
        m=2**64
        h=0
        for ch in reversed(word):
            h=(h*p+ord(ch))%m
        return h

    def get_words(text):
        words=[]
        current=""
        for ch in text.lower():
            if ch.isalnum():
                current+=ch
            else:
                if current!="":
                    words.append(current)
                    current=""
        if current!="":
            words.append(current)
        return words

    r1=requests.get(u1)
    r2=requests.get(u2)

    words1=get_words(r1.text)
    words2=get_words(r2.text)

    freq1={}
    for w in words1:
        if w in freq1:
            freq1[w]+=1
        else:
            freq1[w]=1

    freq2={}
    for w in words2:
        if w in freq2:
            freq2[w]+=1
        else:
            freq2[w]=1


if len(sys.argv)!=3:
    print("Please give two website links.")
    sys.exit()

simhash_compare(sys.argv[1],sys.argv[2])