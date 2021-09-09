import re
import jieba
import jieba.posseg
import collections
import numpy
from PIL import Image
import wordcloud
import matplotlib.pyplot as plt
#2. word frequency
#open and process file

#location WordFrequencyCSR201X(1-4) or WordFrequencySustainabilityBook201X(5-20)
txtOpenfile = 'CSR2014.txt'
txtStopWordDictionary = 'SustainabilityBook2015.txt'
txtWordFrequency = 'WordFrequencySustainabilityBook2015.txt'
number = 100


fn11 = open(txtOpenfile,'r',encoding='UTF-8')
stringData = fn11.read()
fn11.close()
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
stringData = re.sub(pattern, '', stringData)

#Dynamically adjustable dictionary
jieba.suggest_freq('supply chain',True)
jieba.load_userdict('AdjustableDictionary.txt')

#spilt word
segListExact = jieba.cut(stringData,cut_all=False, HMM=True)
objectList = []

#StopWord dictionary
with open(txtStopWordDictionary,'r',encoding='UTF-8') as meaninglessFile:
    stopWords = set(meaninglessFile.read().split('\n'))
stopWords.add(' ')
for word in segListExact:
    if word not in stopWords:
        objectList.append(word)

#wordFrequency
wordCount = collections.Counter(objectList)
wordCountTop = wordCount.most_common(number) #top 'number' word

#output
print('\nword\twordFrequency\twordCharacteristic')
print('------------')
fileOutput = open(txtWordFrequency,'w',encoding='UTF-8')
fileOutput.write('\nword\twordFrequency\twordCharacteristic')
fileOutput.write('--------\n')
count = 0
for topWord, frequency in wordCountTop:
    for POS in jieba.posseg.cut(topWord):
        if count == number:
            break
        print(topWord )
        print(topWord  )
        fileOutput.write(topWord +   '\n')
        count += 1
fileOutput.close()

input()
