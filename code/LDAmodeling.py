#!/usr/bin/env python
# coding: utf-8

import gensim
from gensim import corpora, models
import pickle
from gensim.models.coherencemodel import CoherenceModel
from matplotlib import pyplot as plt
from draw_wordcloud import generate_pic

data = pickle.load(open('phrase_result.pkl', 'rb'))

# Remove the single words
data = list(map(lambda x: [item for item in x if len(item) > 1], data))

# Remove the comments less than 3 words
data = list(filter(lambda x : len(x)>=3, data))

ch_score = []
for k in range(5,31):
    lda_test = models.ldamodel.LdaModel(corpus = corpus, id2word=dictionary, num_topics = k)
    cm = CoherenceModel(model=lda_test, texts=data, dictionary=dictionary, coherence='c_v')
    ch_score.append(cm.get_coherence())
    print(cm.get_coherence())


plt.figure()
plt.xlabel = ('K')
plt.ylable = ('coherence score')
plt.plot(range(5,31),ch_score)
plt.show()


lda27 = models.ldamodel.LdaModel(corpus = corpus, id2word=dictionary, num_topics = 27)
for topic in lda27.print_topics(num_words = 50, num_topics=27):
    print(topic)
lda27.save('lda27.pkl')


#Draw word cloud picture of each topic
generate_pic(lda27, 27, 100)
