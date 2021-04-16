# 18102180 YOGA INDRA WIJAYA IF-06-MM1
# SPAM THRESHOLD = 75%

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

dataset = open("spam.txt","r")
spamlib = dataset.read().split(",")
## print(spamlib)
dataset.close()

msg = "selamat anda mendapatkan pinjaman dengan jumlah yang wow dan wow"
tokens = word_tokenize(msg.lower())
print(tokens)

def vectorize(tokens):
    vector=[]
    for w in spamlib:
        vector.append(tokens.count(w))
    return vector

stopwords = stopwords.words('indonesian')
msg_sw = []
for word in tokens:
    if word not in stopwords:
        msg_sw.append(word)
print(msg_sw)

spam_indicated = []
for word in msg_sw:
    if word in spamlib:
        spam_indicated.append(word)
print(spam_indicated)
print(vectorize(msg_sw))