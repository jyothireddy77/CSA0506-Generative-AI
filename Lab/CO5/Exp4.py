import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()

collection = client.create_collection("documents")

documents = [
    "Artificial intelligence makes machines intelligent.",
    "Python is a programming language.",
    "Machine learning learns from data.",
    "Generative AI creates new content."
]

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=["1", "2", "3", "4"]
)

query = input("Enter query: ")
query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print("\nTop Retrieved Documents:")

for doc in results['documents'][0]:
    print(doc)