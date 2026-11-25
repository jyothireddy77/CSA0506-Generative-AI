from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Artificial intelligence enables machines to perform tasks.",
    "Machine learning allows computers to learn from data.",
    "Python is a popular programming language.",
    "Generative AI creates new content."
]

embeddings = model.encode(documents)

question = input("Ask a question: ")

q = model.encode(question)

scores = util.cos_sim(q, embeddings)

best = scores.argmax().item()

context = documents[best]

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompt = "Answer using this context: " + context + " Question: " + question

answer = generator(prompt, max_new_tokens=100)

print("\nAnswer:", answer[0]['generated_text'])