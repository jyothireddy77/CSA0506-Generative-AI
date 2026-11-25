import re
from collections import Counter
from math import sqrt

documents = [
    "Artificial intelligence enables machines to perform tasks.",
    "Machine learning allows computers to learn from data.",
    "Water conservation reduces water usage.",
    "Leak detection identifies damaged pipelines."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

question = input("Ask a question: ")
q = embed(question)

best = max(documents, key=lambda d: cosine(q, embed(d)))
score = cosine(q, embed(best))

print("\nRetrieved Context:")
print(best)

print("\nAnswer:")
if score > 0:
    print(best)
else:
    print("No relevant information found.")