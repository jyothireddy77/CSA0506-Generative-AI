import os
import re
from collections import Counter
from math import sqrt

folder = "documents"

os.makedirs(folder, exist_ok=True)

sample_files = {
    "ai.txt": "Artificial intelligence enables machines to perform intelligent tasks.",
    "python.txt": "Python is a popular programming language used for development.",
    "ml.txt": "Machine learning allows computers to learn patterns from data.",
    "water.txt": "Smart water systems monitor flow rate, pressure, and water leakage."
}

# Create sample documents
for filename, content in sample_files.items():
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

def embed(text):
    return Counter(re.findall(r"\w+", text.lower()))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in set(a) & set(b))

    na = sqrt(sum(v * v for v in a.values()))
    nb = sqrt(sum(v * v for v in b.values()))

    return dot / (na * nb) if na and nb else 0

# Load documents
documents = []

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        documents.append((filename, content))

print("Multiple Document AI Assistant")
print("Loaded documents:", len(documents))
print("Type 'exit' to stop.")

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    results = []

    for filename, content in documents:
        sentences = [
            s.strip() for s in content.split(".") if s.strip()
        ]

        for sentence in sentences:
            score = cosine(embed(question), embed(sentence))
            results.append((filename, sentence, score))

    results.sort(key=lambda x: x[2], reverse=True)

    if results and results[0][2] > 0:
        filename, answer, score = results[0]

        print("\nAssistant:", answer)
        print("Source Document:", filename)
        print("Similarity Score:", round(score, 3))

    else:
        print("Assistant: No relevant information found.")