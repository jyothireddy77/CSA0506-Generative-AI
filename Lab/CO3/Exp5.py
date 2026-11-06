import re
from collections import Counter
from math import sqrt

documents = [
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Machine learning allows computers to learn from data.",
    "Water conservation reduces unnecessary water usage.",
    "Leak detection identifies damaged water pipelines."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

question = input("Ask a question: ")
q_vector = embed(question)

best_doc = max(
    documents,
    key=lambda doc: cosine(q_vector, embed(doc))
)

score = cosine(q_vector, embed(best_doc))

print("\nRetrieved Context:")
print(best_doc)

print("\nGenerated Answer:")

if score > 0:
    print("Based on the document:", best_doc)
else:
    print("No relevant information was found in the documents.")