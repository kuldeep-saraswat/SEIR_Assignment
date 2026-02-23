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
    def make_hash(url):
        r=requests.get(url)
        words=get_words(r.text)
        freq={}
        for w in words:
            if w in freq:
                freq[w]+=1
            else:
                freq[w]=1
        vec=[0]*64
        for word,count in freq.items():
            h=simple_hash(word)
            for i in range(64):
                if h&(1<<i):
                    vec[i]+=count
                else:
                    vec[i]-=count
        final=0
        for i in range(64):
            if vec[i]>0:
                final|=(1<<i)
        return final
    h1=make_hash(u1)
    h2=make_hash(u2)
    common=0
    for i in range(64):
        if ((h1>>i)&1)==((h2>>i)&1):
            common+=1
    print("Common bits in simhash:",common)

if len(sys.argv)!=3:
    print("Usage: python Similarity.py <url1> <url2>")
    sys.exit()


simhash_compare(sys.argv[1],sys.argv[2])
