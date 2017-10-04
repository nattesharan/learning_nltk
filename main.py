# from nltk.book import *
import nltk
# text1.concordance('name')
# text1.similar('love')
# text2.common_contexts(['monstrous','very'])
# # text1.dispersion_plot(['love'])
# lexical_richness = float(len(set(text5)))/float(len(text5))
# print('Lexical Richness ----> '+str(lexical_richness))
# c = text5.count('lol')
# print(c)
# perc_word = 100 * float(c)/len(text5)
# print('Perc of lol is '+str(perc_word))
# fdist = FreqDist(text1)
# vocabulary = fdist.keys()[:50]
# print(sorted(vocabulary))
# print(fdist['whale'])
# fdist.plot(200, cumulative=True)
# v = set(text5)
# lng = [w for w in v if len(w)>15]
# lng=sorted(lng)
# print(lng)
# fdist = FreqDist(text5)
# lng = [w for w in set(text5) if len(w)>7 and fdist[w]>7]
# print(sorted(lng))
# print(nltk.corpus.gutenberg.fileids())
# emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
# print(len(emma))
# fdist = FreqDist(emma)
# fdist.plot(50,cumulative=True)
# emma.dispersion_plot(['surprize'])
# for geting the number of senteces
# emma_sents = nltk.corpus.gutenberg.sents('austen-emma.txt')
# print(len(emma_sents))
# byrant_sents = nltk.corpus.gutenberg.sents('bryant-stories.txt')
# print(len(byrant_sents))
# working with web text
# print(nltk.corpus.webtext.fileids())
# for webtext in nltk.corpus.webtext.fileids():
#     print webtext,nltk.corpus.webtext.raw(webtext)
# chatroom = nltk.corpus.nps_chat.fileids()
# print(chatroom)
# print(nltk.corpus.brown.categories())
# print(nltk.corpus.brown.words(categories='mystery'))
fic = nltk.corpus.brown.words(categories='fiction')
fdist = nltk.FreqDist([w.lower() for w in fic])
m = ['what','when','where','who','why']
for i in m:
    print i + ':', fdist[i]
