import re
from collections import Counter
from math import sqrt

documents = [
    "Python is a programming language.",
    "Artificial intelligence makes machines intelligent.",
    "Machine learning learns patterns from data.",
    "Water conservation helps protect natural resources."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def similarity(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

# Create an in-memory vector database
vector_database = []

for document in documents:
    vector_database.append({
        "document": document,
        "vector": embed(document)
    })

query = input("Enter your query: ")
query_vector = embed(query)

results = []

for item in vector_database:
    score = similarity(query_vector, item["vector"])
    results.append((item["document"], score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nRetrieved Documents:")

for document, score in results[:3]:
    print(document, "| Score:", round(score, 3))