# 18102180 YOGA INDRA WIJAYA IF-06-MM1
# THRESHOLD = 75%

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# memanggil dataset
dataset = open("spam.txt","r")
spamlib = dataset.read().split(",")
## print(spamlib)
dataset.close()

# input teks untuk deteksi spam
msg = input('masukkan pesan : ')
tokens = word_tokenize(msg.lower())
print(tokens)

# fungsi untuk vektor
def vectorize(tokens):
    vector=[]
    for w in spamlib:
        vector.append(tokens.count(w))
    return vector

# pre-process - membersihkan stop words dari input
stopwords = stopwords.words('indonesian')
msg_sw = []
for word in tokens:
    if word not in stopwords:
        msg_sw.append(word)
print(msg_sw)

# process - menghitung kata yang mengandung spam, dan vektorisasi
spam_indicated = []
notSpam = []
for word in msg_sw:
    if word in spamlib:
        spam_indicated.append(word)
    else : notSpam.append(word)
print(spam_indicated)
print(notSpam)
vector = vectorize(msg_sw)
print(vector[:5])

# result - kesimpulan
if len(spam_indicated) == len(notSpam): res = 50
else: res = round(len(spam_indicated)/len(notSpam)*100)

if res > 75: kesimpulan = "SPAM"
else: kesimpulan = "BUKAN SPAM"

print(str(res)+"% spam")
print("dengan threshold 75% maka disimpulan pesan ini termasuk " + kesimpulan)