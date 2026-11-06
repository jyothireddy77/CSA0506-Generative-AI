import re
from collections import Counter
from math import sqrt

documents = [
    "Artificial intelligence is a technology that enables machines to perform tasks. "
    "It is used in healthcare, education, and business.",

    "Machine learning is a part of artificial intelligence. "
    "It learns patterns from data and makes predictions.",

    "Water management includes monitoring water supply. "
    "Leak detection helps prevent water loss."
]

def chunk_text(text):
    sentences = text.split(". ")
    return [s.strip() for s in sentences if s.strip()]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

# Document chunking
chunks = []

for doc in documents:
    chunks.extend(chunk_text(doc))

# Query processing
question = input("Ask your question: ")
q_vector = embed(question)

# Retrieval
ranked = sorted(
    chunks,
    key=lambda chunk: cosine(q_vector, embed(chunk)),
    reverse=True
)

context = ranked[:2]

print("\nRetrieved Context:")

for item in context:
    print("-", item)

# Answer generation
print("\nFinal Answer:")

if context and cosine(q_vector, embed(context[0])) > 0:
    print(" ".join(context))
else:
    print("No relevant answer found in the documents.")