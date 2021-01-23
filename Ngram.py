import nltk
from nltk.util import ngrams
from collections import Counter
import re
import csv
import bs4 as bs
import urllib.request


file = urllib.request.urlopen('https://ta.wikipedia.org/wiki/%E0%AE%A4%E0%AE%A9%E0%AE%BF%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%9F%E0%AF%8D%E0%AE%9F_%E0%AE%B5%E0%AE%BE%E0%AE%B4%E0%AF%8D%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%88')
file = file.read()


content = bs.BeautifulSoup(file, 'lxml')
paragraphs = content.find_all('p')
text = ''

for para in paragraphs:
    text += para.text
    

def SpecialCharacterRemoval(content):
    result = re.sub(r"['[['(',')'@\'?\.:;$%_]", "", text)
    result = result.replace(']', r"")
    return(result)

def writefile(num,Out):
    res="result"+str(num)+"."+"csv"
    print(res)
    with open(res, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for i in Out:
            writer.writerow(i)    


def Findgrams(file,num):
    d=SpecialCharacterRemoval(file)
    token = nltk.word_tokenize(d)
    Ngrams= ngrams(token,num)
    Out=Counter(Ngrams)
    Max_Out=Out.most_common(10)
    writefile(num,Max_Out)
    
Findgrams(text,1)
Findgrams(text,2)