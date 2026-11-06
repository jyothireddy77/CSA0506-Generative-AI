import re
from collections import Counter
from math import sqrt

documents = [
    "Python is a programming language.",
    "Machine learning helps computers learn from data.",
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Generative AI creates text, images, and other content."
]

history = []

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

print("Context-Aware Chatbot")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    context = " ".join(history[-2:])
    combined_query = context + " " + question

    query_vector = embed(combined_query)

    best = max(
        documents,
        key=lambda doc: cosine(query_vector, embed(doc))
    )

    score = cosine(query_vector, embed(best))

    if score > 0:
        answer = best
    else:
        answer = "Sorry, I could not find relevant information."

    print("Chatbot:", answer)

    history.append(question)