import re
from collections import Counter
from math import sqrt

documents = [
    "Python is a programming language.",
    "Artificial intelligence makes machines intelligent.",
    "Machine learning learns from data.",
    "Water conservation protects resources."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

database = []

for doc in documents:
    database.append((doc, embed(doc)))

query = input("Enter query: ")
q = embed(query)

results = []

for doc, vector in database:
    score = cosine(q, vector)
    results.append((doc, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nRetrieved Documents:")
for doc, score in results[:3]:
    print(doc, round(score, 3))