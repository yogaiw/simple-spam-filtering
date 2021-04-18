# 18102180 YOGA INDRA WIJAYA S1IF-06-MM1

import pandas as pd
import string
import nltk

### MEMANGGIL DATASET KOLEKSI PESAN SPAM DALAM BAHASA INDONESIA
dataset = pd.read_csv('dataset.txt', sep = '\t', header=None, names=["label","msg"])
# print(dataset.head()) #untuk debugging

### PRE-PROCESSING - MELAKUKAN TOKENISASI DAN MENGHAPUS STOPWORDS
stopwords = nltk.corpus.stopwords.words('indonesian')
punctuation = string.punctuation

def pre_process(msg):
    remove_punct = "".join([word.lower() for word in msg if word not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords

### MENGKATEGORIKAN KATA-KATA YANG MENGANDUNG SPAM DAN TIDAK SPAM
def categorize_words():
    spam_words = []
    ham_words = []
    
    for msg in dataset['processed'][dataset['label'] == 'spam']:
        for word in msg:
            spam_words.append(word)

    for msg in dataset['processed'][dataset['label'] == 'ham']:
        for word in msg:
            ham_words.append(word)
    return spam_words, ham_words

def predict(msg):
    spam_counter = 0
    ham_counter = 0
    
    for word in msg:
        spam_counter += spam_words.count(word)
        ham_counter += ham_words.count(word)
    print('***RESULTS***')
    
    if ham_counter > spam_counter:
        accuracy = round((ham_counter / (ham_counter + spam_counter) * 100))
        print('bukan spam, {}% yakin'.format(accuracy))
    
    elif ham_counter == spam_counter:
        print('pesan ini bisa saja spam')
        
    else:
        accuracy = round((spam_counter / (ham_counter + spam_counter)* 100))
        print('message is spam, {}% yakin'.format(accuracy))

dataset['processed'] = dataset['msg'].apply(lambda x: pre_process(x))
# print(dataset['processed'].head()) # untuk debugging
spam_words, ham_words = categorize_words()
# print(spam_words[:5]) # untuk debugging
# print(ham_words[:5]) # untuk debugging

user_input = input("Input Pesan : ")
processed_input = pre_process(user_input)
predict(processed_input)