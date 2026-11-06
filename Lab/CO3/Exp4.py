import re
from collections import Counter
from math import sqrt

documents = [
    "Water is essential for human life.",
    "Smart water systems monitor water flow.",
    "Leak detection helps reduce water loss.",
    "Artificial intelligence supports automation.",
    "Machine learning analyzes sensor data."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

query = input("Enter your query: ")

k = int(input("Enter top-K value: "))

if k <= 0:
    print("K must be greater than zero.")

else:
    query_vector = embed(query)
    results = []

    for doc in documents:
        score = cosine(query_vector, embed(doc))
        results.append((doc, score))

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop", k, "Retrieved Documents:")

    for doc, score in results[:k]:
        print(doc)
        print("Score:", round(score, 3))