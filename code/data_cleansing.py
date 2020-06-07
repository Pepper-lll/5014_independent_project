#!/usr/bin/env python
# coding: utf-8

import string
from zhon.hanzi import punctuation
import jsonlines
import pickle
import jieba

n = 0
with open("disc.jl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        n +=1
print(n)


with open("disc.jl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
#         print(item)
        pass



## get the contents
allcontent = []
with open("disc.jl", "r+", encoding="utf8") as f:    
    for item in jsonlines.Reader(f):
        allcontent.append(item['content'])
print('length of the raw data:' ,len(allcontent))


#delete the emtpy content
allcontent = list(filter(lambda x: len(x) > 0, allcontent))
print('number of contents with words:', len(allcontent))



# only kept Chinese and Engilish words
def is_word(uchar):
    if (uchar >= u'\u4e00' and uchar <= u'\u9fa5') or (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a') or uchar==' ':
        return True
    else:
        return False

def format_str(content):
    content_str = ''
    for i in content:
        if is_word(i):
            content_str = content_str + ｉ
    return content_str

onlyword_c = []
for line in allcontent:
    onlyword_c.append(format_str(line[0]))

pickle.dump(onlyword_c, open('onlyword_c.pkl', 'wb'))



# load Cantonese corpus
jieba.load_userdict("./data/dict.txt")

cutted_l= []
for s in onlyword_c:
    cutted_l.append((','.join(jieba.cut(s, HMM=False))))


def is_letter(s):
    for c in s:
        if not((c >= u'\u0041' and c<=u'\u005a') or (c >= u'\u0061' and c <=u'\u007a')):
            return False
    return True


#combine the English words back together
for i in range(len(cutted_l)):
    tmp = cutted_l[i].split(',')
    new_s = []
    idx = 0
    while idx < len(tmp):
        if is_letter(tmp[idx]):
            start_idx = idx
            idx += 1
            while idx < len(tmp) and is_letter(tmp[idx]):
                idx += 1
            eng_word = ''.join(tmp[start_idx:idx])
            new_s.append(eng_word)
        else:
            new_s.append(tmp[idx])
        idx += 1
    cutted_l[i] = ','.join(new_s)

for i in range(len(cutted_l)):
    cutted_l[i] = cutted_l[i].replace(', ','')


#word segmentation result with Cantonese corpus
with open('processed_data.txt', 'w') as f:
    f.write(str(cutted_l))
    f.close()
with open('processed_data.txt', 'r') as f:
    print(len(eval(f.read())))
    f.close()



d = onlyword_c.copy()
#Remove the contents less than 10 words
d = list(filter(lambda x: len(x) >= 10, d))
print('The number of contents with more than 10 words:', len(d))

#Remove Duplicates
d=list(set(d))
print('The number of contents with more than 10 words and without duplicates:', len(d))

#Get the result
pickle.dump(d, open('content_len10.pkl', 'wb'))





