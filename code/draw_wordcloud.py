# -*- encoding: utf-8 -*-
from gensim.models.ldamodel import LdaModel
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_pic(model, num_topics=27, num_words=100, output_file='./result'):
    res = model.print_topics(num_topics=num_topics, num_words=num_words)
    # Extraction
    word_clouds = []
    for topic in res:
        l = topic[1].split('+')
        tmp = []
        for word in l:
            num, w = word.split('*')
            tmp.append((int(float(num)*1000), w[1:-2]))
        word_clouds.append(tmp)
    # Form texts
    word_cloud_texts = []
    for cloud in word_clouds:
        texts = []
        for word in cloud:
            for i in range(word[0]):
                texts.append(word[1])
        word_cloud_texts.append(' '.join(texts))
    # Draw
    for idx, word_text in enumerate(word_cloud_texts):
        wordcloud = WordCloud(scale=64, font_path='./SNsanafonGyou.ttf', background_color="white",
                              max_font_size=100, collocations=False).generate(word_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(f'./word_cloud_pics/{idx}.png', dpi=800)





# In[ ]:




