import numpy as np


def cosine_similarity(sentence_vector,query_vector):
    """
    Calculate the cosine similarity between the given sentence vector and query vector.

    Parameters:
    sentence_vector (array-like): The vector representation of a sentence.
    query_vector (array-like): The vector representation of a query.

    Returns:
    float: The cosine similarity between the two input vectors.
    """
    return np.dot(sentence_vector,query_vector)/(np.linalg.norm(sentence_vector)*np.linalg.norm(query_vector))   


def manhattan_distance(sentence_vector,query_vector):

    return np.linalg.norm(sentence_vector-query_vector)

# a = np.array([4,0,3])
# b = np.array([4,0,2])
# print(a-b)