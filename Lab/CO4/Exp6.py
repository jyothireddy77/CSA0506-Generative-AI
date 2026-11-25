import re
from collections import Counter
from math import sqrt

documents = [
    "AI enables machines to perform tasks. AI is used in healthcare.",
    "Machine learning learns patterns from data. It makes predictions.",
    "Water management monitors water supply. Leak detection prevents loss."
]

def chunk_text(text):
    return [s.strip() for s in text.split(".") if s.strip()]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

chunks = []

for doc in documents:
    chunks.extend(chunk_text(doc))

question = input("Ask a question: ")
q = embed(question)

results = sorted(
    chunks,
    key=lambda x: cosine(q, embed(x)),
    reverse=True
)

print("\nRetrieved Context:")

for item in results[:2]:
    print(item)

print("\nGenerated Answer:")

if results and cosine(q, embed(results[0])) > 0:
    print(results[0])
else:
    print("No relevant answer found.")