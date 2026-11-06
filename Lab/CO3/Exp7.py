import re
from collections import Counter
from math import sqrt

knowledge = [
    "Water distribution systems supply water to different areas.",
    "Pipelines transport water from reservoirs to consumers.",
    "Water pressure is important for proper distribution.",
    "Leak detection helps identify damaged pipelines.",
    "Smart sensors monitor flow rate and pressure."
]

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

print("Water Management Chatbot")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    q_vector = embed(question)

    best = max(
        knowledge,
        key=lambda item: cosine(q_vector, embed(item))
    )

    score = cosine(q_vector, embed(best))

    if score > 0:
        print("Chatbot:", best)
    else:
        print("Chatbot: Sorry, I do not have information about that topic.")