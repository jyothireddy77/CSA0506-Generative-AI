import re
from collections import Counter
from math import sqrt

knowledge = [
    "Water distribution supplies water to different areas.",
    "Pipelines transport water to consumers.",
    "Water pressure is important for distribution.",
    "Leak detection identifies damaged pipelines.",
    "Sensors monitor water flow and pressure."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

print("Water Management Chatbot")
print("Type exit to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    q = embed(question)

    best = max(knowledge, key=lambda x: cosine(q, embed(x)))
    score = cosine(q, embed(best))

    if score > 0:
        print("Bot:", best)
    else:
        print("Bot: No relevant information found.")