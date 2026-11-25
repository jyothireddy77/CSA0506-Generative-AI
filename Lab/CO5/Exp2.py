from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "AI is used in healthcare.",
    "Machine learning analyzes data.",
    "Python is used for programming.",
    "AI helps doctors identify diseases."
]

doc_embeddings = model.encode(documents)

query = input("Enter search query: ")
query_embedding = model.encode(query)

scores = util.cos_sim(query_embedding, doc_embeddings)

results = scores[0].argsort(descending=True)

print("\nSearch Results:")

for i in results:
    print(documents[i], round(scores[0][i].item(), 3))