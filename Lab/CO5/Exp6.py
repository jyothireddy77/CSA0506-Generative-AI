from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "AI is used in healthcare.",
    "Machine learning analyzes data.",
    "Python is a programming language.",
    "Water conservation saves resources."
]

chunks = []

for doc in documents:
    chunks.extend(doc.split("."))

chunks = [c.strip() for c in chunks if c.strip()]

embeddings = model.encode(chunks)

question = input("Enter your question: ")

q = model.encode(question)

scores = util.cos_sim(q, embeddings)

top = scores[0].topk(2).indices.tolist()

context = " ".join([chunks[i] for i in top])

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompt = "Context: " + context + " Question: " + question

answer = generator(prompt, max_new_tokens=100)

print("\nRetrieved Context:", context)
print("\nGenerated Answer:", answer[0]['generated_text'])