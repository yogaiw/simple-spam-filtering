import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

msg = "Selamat anda mendapatkan hadiah sebesar 10 juta"

tokens = word_tokenize(msg)
print(tokens)

stopwords = stopwords.words('indonesian')
msg_sw = []

for word in tokens:
    if word not in stopwords:
        msg_sw.append(word)

print(msg_sw)