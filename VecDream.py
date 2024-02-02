from utilities import cosine_similarity, manhattan_distance


class VecDream():
    def __init__(self):
        self.vector_store  = {}

    def addVectors(self,sentence_with_vectors:dict):
        for tokens,embeddings in sentence_with_vectors.items():
            if tokens not in self.vector_store.keys():
                self.vector_store[tokens] = embeddings
            

    def getallVectors(self):
        return self.vector_store

    def getVector(self,sentence):
        return self.vector_store.get(sentence)
    
    def getSentence(self,vector):
        return [key for key, value in self.vector_store.items() if value == vector]
    
    def askQuery(self,query_vector,num_results=1):
        scores = {}
        query_vector =query_vector[0]
        for sentence,vector in self.vector_store.items():
            scores[sentence] = cosine_similarity(query_vector,vector)
        print(scores)
        return sorted(scores.items(),key=lambda x:x[1],reverse=True)[:num_results]
    