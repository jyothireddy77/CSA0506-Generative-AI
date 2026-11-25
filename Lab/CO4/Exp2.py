import re
from collections import Counter
from math import sqrt

documents = {
    "Doc1": "Artificial intelligence is used in healthcare.",
    "Doc2": "Machine learning analyzes data.",
    "Doc3": "Python is used for programming.",
    "Doc4": "AI helps doctors identify diseases."
}

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

query = input("Enter search query: ")
q = embed(query)

results = []

for name, doc in documents.items():
    score = cosine(q, embed(doc))
    results.append((name, doc, score))

results.sort(key=lambda x: x[2], reverse=True)

for name, doc, score in results:
    print(name, doc, round(score, 3))