import re
from collections import Counter
from math import sqrt

document = """
Artificial intelligence enables machines to perform intelligent tasks.
Python is a popular programming language.
Machine learning helps computers learn from data.
Generative AI creates new content such as text and images.
"""

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

sentences = [
    s.strip() for s in document.split(".") if s.strip()
]

print("Document AI Assistant")
print("Type 'exit' to stop.")

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("Assistant: Thank you!")
        break

    best = max(
        sentences,
        key=lambda s: cosine(embed(question), embed(s))
    )

    score = cosine(embed(question), embed(best))

    if score > 0:
        print("Assistant:", best)
    else:
        print("Assistant: No matching information found.")