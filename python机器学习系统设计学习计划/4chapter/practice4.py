from gensim import corpora,models,similarities
corpus = corpora.BleiCorpus('./data/ap/ap.dat','./data/ap/vocab.txt')
print(corpus)