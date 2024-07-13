from gensim.models import Word2Vec

# サンプルデータ
sentences = [
    ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],
    ['I', 'love', 'to', 'play', 'football'],
    ['artificial', 'intelligence', 'and', 'machine', 'learning', 'are', 'fascinating'],
    ['the', 'dog', 'barked', 'at', 'the', 'mailman'],
    ['he', 'is', 'learning', 'to', 'play', 'guitar']
]

# モデルのトレーニング
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 単語ベクトルの取得
word_vector = model.wv['football']
print(f"Vector for 'football': {word_vector}")

# 類似単語の検索
similar_words = model.wv.most_similar('football')
print("Words similar to 'football':")
for word, similarity in similar_words:
    print(f"{word}: {similarity}")

# 単語間の類似度の計算
similarity = model.wv.similarity('football', 'play')
print(f"Similarity between 'football' and 'play': {similarity}")

# モデルの保存
model.save("word2vec.model")

# モデルの読み込み
loaded_model = Word2Vec.load("word2vec.model")

# 保存されたモデルで類似単語の検索
loaded_similar_words = loaded_model.wv.most_similar('football')
print("Words similar to 'football' using loaded model:")
for word, similarity in loaded_similar_words:
    print(f"{word}: {similarity}")
