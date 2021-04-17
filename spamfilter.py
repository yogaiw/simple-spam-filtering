# 18102180 YOGA INDRA WIJAYA IF-06-MM1
# SPAM THRESHOLD = 75%

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# memanggil dataset
dataset = open("spam.txt","r")
spamlib = dataset.read().split(",")
## print(spamlib)
dataset.close()

# input teks untuk deteksi spam
msg = "Selamat anda mendapatkan kesempatan pinjaman dengan jumlah yang wow, jangan sia siakan kesempatan ini, anda dapat melakukan kredit motor secara cepat"
tokens = word_tokenize(msg.lower())
print(tokens)

# fungsi untuk vektor
def vectorize(tokens):
    vector=[]
    for w in spamlib:
        vector.append(tokens.count(w))
    return vector

# membersihkan stop words dari input
stopwords = stopwords.words('indonesian')
msg_sw = []
for word in tokens:
    if word not in stopwords:
        msg_sw.append(word)
print(msg_sw)

# menghitung kata yang mengandung spam, dan vektorisasi
spam_indicated = []
for word in msg_sw:
    if word in spamlib:
        spam_indicated.append(word)
print(spam_indicated)
vector = vectorize(msg_sw)
print(vector)

def result(v):
    spam_contain_count = sum(v)*20
    return spam_contain_count

print(str(result(vector))+"%")