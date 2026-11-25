import re
from collections import Counter
from math import sqrt

sentences = [
    "Artificial intelligence makes machines intelligent.",
    "Machine learning helps computers learn from data.",
    "Python is a programming language.",
    "Generative AI creates new content."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

query = input("Enter search query: ")
q = embed(query)

results = [(s, cosine(q, embed(s))) for s in sentences]
results.sort(key=lambda x: x[1], reverse=True)

print("\nMost Similar Sentences:")
for sentence, score in results:
    print(sentence, ":", round(score, 3))