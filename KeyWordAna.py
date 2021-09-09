
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

#location CSR2011.txt or SustainabilityBook2015.txt
#location WordFrequencyCSR2011.txt or WordFrequencySustainabilityBook2015.txt
txtOpenfile = 'CSR2011.txt'
txtStopWordDictionary = 'StopWordDictionary.txt'
txtWordFrequency = 'WordFrequencyCSR2011.txt'
pictureWordCloud = 'word cloud 2011.png'
number = 100

fn11 = open(txtOpenfile,'r',encoding='UTF-8')
stringData = fn11.read()
stringData= stringData.lower()
fn11.close()
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
stringData = re.sub(pattern, '', stringData)

#Dynamically adjustable dictionary

jieba.load_userdict('AdjustableDictionary.txt')

#sgment word
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
print('\nword\twordFrequency')
print('------------')
fileOutput = open(txtWordFrequency,'w',encoding='UTF-8')
fileOutput.write('\nword\twordFrequency')
fileOutput.write('--------\n')
count = 0
for topWord, frequency in wordCountTop:
    for POS in jieba.posseg.cut(topWord):
        if count == number:
            break
        print(topWord + '\t', str(frequency) + '\t')
        fileOutput.write(topWord + '               ' + str(frequency) + '              ' +  '\n')
        count += 1
fileOutput.close()

#wordCloud wc:wordCloud
print('\nword cloud')
wc = wordcloud.WordCloud(background_color='white',max_words=number,max_font_size=150)

wc.generate_from_frequencies(wordCount)
plt.figure('word cloud')
plt.subplots_adjust(top=0.99,bottom=0.01, right=0.99, left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

#pic save
wc.to_file(pictureWordCloud)

input()






















