import os
import re
from collections import Counter
from math import sqrt

folder = "documents"
os.makedirs(folder, exist_ok=True)

sample_files = {
    "ai.txt": "Artificial intelligence makes machines intelligent.",
    "python.txt": "Python is a programming language.",
    "ml.txt": "Machine learning learns from data.",
    "water.txt": "Smart systems monitor water leakage."
}

for name, content in sample_files.items():
    path = os.path.join(folder, name)

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0

documents = []

for name in os.listdir(folder):
    if name.endswith(".txt"):
        with open(os.path.join(folder, name), "r", encoding="utf-8") as f:
            documents.append((name, f.read()))

print("Multiple Document AI Assistant")
print("Type exit to stop.")

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    results = []

    for name, content in documents:
        for sentence in content.split("."):
            sentence = sentence.strip()

            if sentence:
                score = cosine(embed(question), embed(sentence))
                results.append((name, sentence, score))

    results.sort(key=lambda x: x[2], reverse=True)

    if results and results[0][2] > 0:
        name, answer, score = results[0]
        print("Assistant:", answer)
        print("Source:", name)
    else:
        print("Assistant: No relevant information found.")