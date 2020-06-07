#!/usr/bin/env python
# coding: utf-8

# -*- encoding: utf-8 -*-
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases, Phraser
import pickle
import jieba

data = pickle.load(open('for_phrases.pkl', 'rb'))
phrases = Phrases(data, min_count=10, threshold=0.1, scoring='npmi')

# for phrase, score in phrases.export_phrases(test):
#     print(phrase.decode(), score)

# for key, val in phrases.vocab.items():
#        print(key.decode(), val)

bigram = Phraser(phrases)

for i in test[:10]:
    print(bigram[i])


# remove stopwords first, then detect phrase

# In[10]:

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

#load Cantonese stopwords
stopwords = stopwordslist('/Users/liuxuantong/BDT_in_HKUST/5014_independent_project/data/stopwords.txt')
for i in range(len(data)):
    tmp = [w for w in test[i] if w not in stopwords]
    data[i] = tmp


# In[91]:


pickle.dump(data, open('for_phrase_nosw.pkl', 'wb'))


# ## See all resluts
# all_phrases = Phrases(data, min_count=10, threshold=-1, scoring='npmi')
# for phrase, score in all_phrases.export_phrases(data):
#     print(phrase.decode(), score)


# * Pointwise mutual information can be normalized between [-1,+1] resulting in -1 (in the limit) for never occurring together, 0 for independence, and +1 for complete co-occurrence.
# * set threshold=0.1
phrases = Phrases(data, min_count=10, threshold=0.1, scoring='npmi')


# for phrase, score in phrases.export_phrases(test):
#     print(phrase.decode(), score)


bigram = Phraser(phrases)
# print(data[:10])

# for i in data[:10]:
#     print(bigram[i])


result = []
for i in test:
    result.append(bigram[i])

pickle.dump(result, open('phrases_res_nost.pkl','wb'))


### based on bigram phrases to detect trigram and 4-grams
bg = pickle.load(open('phrases_res_nost.pkl', 'rb'))
phrases2 = Phrases(bg, min_count=10, threshold=0.1, scoring = 'npmi')

phr_score = {}
for phrase, score in phrases2.export_phrases(bg):
#     print(phrase.decode(), score)
    phr_score[phrase.decode()] = score


print('The npmi score of phrases:' 
    sorted(phr_score.items(), key=lambda d: d[1], reverse=True))


trigram = Phraser(phrases2)
# for i in bg[:100]:
#     print(trigram[i])
bi_tri_res = []
for i in bg:
    bi_tri_res.append(trigram[i])


for i in range(len(bi_tri_res)):
    for j in range(len(bi_tri_res[i])):
        bi_tri_res[i][j] = bi_tri_res[i][j].replace('_','')

pickle.dump(bi_tri_res, open('phrase_result.pkl', 'wb'))







