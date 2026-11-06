import re
from collections import Counter
from math import sqrt

documents = {
    "Document 1": "Artificial intelligence is used in healthcare.",
    "Document 2": "Machine learning is useful for data analysis.",
    "Document 3": "Python is used for software development.",
    "Document 4": "AI helps doctors identify diseases."
}

def vector(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

query = input("Enter your search query: ")
query_vector = vector(query)

results = []

for name, content in documents.items():
    score = cosine(query_vector, vector(content))
    results.append((name, content, score))

results.sort(key=lambda x: x[2], reverse=True)

print("\nSearch Results:")

for name, content, score in results:
    print(name, "-", content)
    print("Similarity:", round(score, 3))