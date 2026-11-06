import re
from collections import Counter
from math import sqrt

sentences = [
    "Artificial intelligence makes machines intelligent.",
    "Machine learning helps computers learn from data.",
    "Python is a popular programming language.",
    "Generative AI creates new text and images."
]

def embed(text):
    words = re.findall(r"\w+", text.lower())
    return Counter(words)

def cosine_similarity(a, b):
    common = set(a) & set(b)
    dot = sum(a[w] * b[w] for w in common)

    norm_a = sqrt(sum(v * v for v in a.values()))
    norm_b = sqrt(sum(v * v for v in b.values()))

    return dot / (norm_a * norm_b) if norm_a and norm_b else 0

query = input("Enter your search query: ")
query_vector = embed(query)

scores = [
    (s, cosine_similarity(query_vector, embed(s)))
    for s in sentences
]

scores.sort(key=lambda x: x[1], reverse=True)

print("\nMost similar sentence:")

if scores and scores[0][1] > 0:
    print(scores[0][0])
    print("Similarity score:", round(scores[0][1], 3))
else:
    print("No similar sentence found.")