from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("document.txt", "r", encoding="utf-8") as f:
    text = f.read()

documents = [s.strip() for s in text.split(".") if s.strip()]

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