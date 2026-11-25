from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Artificial intelligence makes machines intelligent.",
    "Machine learning learns from data.",
    "Python is a programming language.",
    "Generative AI creates new content."
]

embeddings = model.encode(sentences)

query = input("Enter search query: ")
query_embedding = model.encode(query)

scores = util.cos_sim(query_embedding, embeddings)

for i, score in enumerate(scores[0]):
    print(sentences[i], ":", round(score.item(), 3))

best = scores.argmax().item()
print("\nMost Similar:", sentences[best])