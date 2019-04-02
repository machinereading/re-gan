from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import pickle

print("Loading word2vec...")
# wv_model = KeyedVectors.load_word2vec_format("../../data/kaist/embedding/fasttext/wiki_model.vec")
wv_model = KeyedVectors.load('../../data/kaist/embedding/word2vec/word2vec.kv', mmap='r')

D = wv_model.vocab
vocab = []
for key, value in D.items():
    vocab.append(key)

with open('../../data/kaist/embedding/word2vec/word2vec_100d_wikipedia.pkl', 'wb') as f:
    pickle.dump((wv_model.vectors, vocab), f)

print(len(wv_model.vectors[0]))
print(len(vocab))