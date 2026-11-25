import re
from collections import Counter
from math import sqrt

document = """
Artificial intelligence enables machines to perform tasks.
Python is a popular programming language.
Machine learning learns from data.
Generative AI creates text and images.
"""

sentences = [s.strip() for s in document.split(".") if s.strip()]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

print("AI Document Assistant")
print("Type exit to stop.")

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    best = max(sentences, key=lambda x: cosine(embed(question), embed(x)))
    score = cosine(embed(question), embed(best))

    if score > 0:
        print("Assistant:", best)
    else:
        print("Assistant: No matching information found.")