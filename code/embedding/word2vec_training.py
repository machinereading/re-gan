from gensim.models.word2vec import Word2Vec
import codecs
import multiprocessing

config = {
    'min_count': 5,  # 등장 횟수가 5 이하인 단어는 무시
    'size': 100,  # 300차원짜리 벡터스페이스에 embedding
    'sg': 1,  # 0이면 CBOW, 1이면 skip-gram을 사용한다
    'batch_words': 10000,  # 사전을 구축할때 한번에 읽을 단어 수
    'workers': 1, #multiprocessing.cpu_count(),
}

class SentenceReader:

    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            yield line.split(' ')

sentences_vocab = SentenceReader("../../data/kaist/embedding/wikilinkCorpus_wv.txt")
sentences_train = SentenceReader("../../data/kaist/embedding/wikilinkCorpus_wv.txt")

print("Finished corpus loading.")
model = Word2Vec(**config)
print("Build sentence vocab.")
model.build_vocab(sentences_vocab, update=False)
print("Finished vocab building, and Training word2vec embedding.")
model.train(sentences_train, total_examples=model.corpus_count, epochs=1)
print("Finished model training.")
model.most_similar(positive=["한국/Noun", "도쿄/Noun"], negative=["서울/Noun"], topn=3)
model.save("../../data/kaist/embedding/word2vec/word2vec.model")
print("Finished model save.")

model = Word2Vec.load('../../data/kaist/embedding/word2vec/word2vec.model')
print(model.most_similar(positive=["이순신/Entity"], topn=3))
print(model.most_similar(positive=["김연아/Entity"], topn=3))

word_vectors = model.wv
word_vectors.save('../../data/kaist/embedding/word2vec/word2vec.kv')