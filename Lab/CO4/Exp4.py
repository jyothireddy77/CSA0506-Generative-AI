import re
from collections import Counter
from math import sqrt

documents = [
    "Water is essential for life.",
    "Smart systems monitor water flow.",
    "Leak detection reduces water loss.",
    "AI supports automation.",
    "Machine learning analyzes data."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

query = input("Enter query: ")
k = int(input("Enter K value: "))

q = embed(query)

results = []

for doc in documents:
    score = cosine(q, embed(doc))
    results.append((doc, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nTop-K Documents:")

for doc, score in results[:k]:
    print(doc, round(score, 3))