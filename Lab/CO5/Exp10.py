import os
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

model = SentenceTransformer('all-MiniLM-L6-v2')

folder = "documents"

documents = []
sources = []

for file in os.listdir(folder):
    if file.endswith(".txt"):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            text = f.read()

        for sentence in text.split("."):
            if sentence.strip():
                documents.append(sentence.strip())
                sources.append(file)

embeddings = model.encode(documents)

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

question = input("Ask a question: ")

q = model.encode(question)

scores = util.cos_sim(q, embeddings)

top = scores[0].argmax().item()

context = documents[top]

prompt = "Context: " + context + " Question: " + question

answer = generator(prompt, max_new_tokens=100)

print("\nAssistant:", answer[0]['generated_text'])
print("Source:", sources[top])