import re
from collections import Counter
from math import sqrt

documents = [
    "Python is a programming language.",
    "Machine learning learns from data.",
    "Artificial intelligence makes machines intelligent.",
    "Generative AI creates new content."
]

history = []

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

print("Context-Aware Chatbot")
print("Type exit to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    context = " ".join(history[-2:])
    query = context + " " + question

    q = embed(query)

    best = max(documents, key=lambda x: cosine(q, embed(x)))
    score = cosine(q, embed(best))

    if score > 0:
        print("Bot:", best)
    else:
        print("Bot: No relevant information found.")

    history.append(question)