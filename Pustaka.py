# Import library for help our project
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import re
from Data import fix_data,nomor,nama


# parsing and cleaning data to dataframe

nama = [a.lower().title() for a in nama]
clean_data = [re.sub('\t|,',' ',a.lower()) for a in fix_data]
df = pd.DataFrame({'index':[a for a in range(len(clean_data))],'demografik_dosen':clean_data})

df['nomor'] = nomor
df['nama'] = nama

# Our OOP's project, the brain of our main program

class Mesin_pencari():
    
    def __init__(self,data,df):
        self.model = TfidfVectorizer(ngram_range=(1,15))
        self.dataframe = df
        self.data = data
        self.bank = None
        self.encode = None
    
    def fit(self):
        self.model.fit(self.data)
        self.bank = self.model.transform(self.data)
        
    def predict(self,array_of_):
        x = [a.lower() for a in array_of_]
        cos = cosine_similarity(self.model.transform(x),self.bank).argsort()[0][len(self.data) - 1]
        return (self.dataframe[self.dataframe['index'] == cos].nomor.values[0],
                self.dataframe[self.dataframe['index'] == cos].nama.values[0])

def jalankan():
    l = []
    M = Mesin_pencari(df.demografik_dosen,df)
    M.fit()
    quest = input('nomor dosen siapa yang anda cari?\n')
    l.append(quest)
    nomor,nama = M.predict(l)
    quest2 = input("apakah benar nama dosen ini yang anda cari {nama}? [tekan n untuk melanjutkan dan tekan sembarang jika itu bukan nama dosen yang anda cari]\n".format(nama = nama))
    if quest2.lower() == 'n':
        print('nomor dari dosen {} adalah {}\n'.format(nama,nomor))
    else:
        print('silahkankan perbaiki keyword anda dengan kata-kata yang lebih spesifik\n')
        

# And last we must make a definition for running program, it's ez just like while a program with looping argument

if __name__ == '__main__':
    while True:
        quest = input('apakah anda ingin memulai program ? tekan y untuk memulai dan tekan x untuk keluar \n')
        if quest.lower() == 'y':
            jalankan()
        else:
            print('anda keluar dari program \n')
            break
