# from VecDream import VecDream

from sentence_transformers import SentenceTransformer
# import VecDream
from VecDream import VecDream

client = VecDream()


model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.']

sentence_embeddings = model.encode(sentences)

sentence_vectors = dict()

for sentence, embedding in zip(sentences, sentence_embeddings):
    sentence_vectors[sentence] = embedding

client.addVectors(sentence_vectors)


# for sen,tok in client.getallVectors().items():
    # print("Sentence",sen)

    # print("Emb",type(tok))


import time

prev = time.time()

query = ["The swift brown fox leaps over the lethargic dog."]

query_vector = model.encode(query)

print(client.askQuery(query_vector,num_results=3))

print(time.time()-prev)