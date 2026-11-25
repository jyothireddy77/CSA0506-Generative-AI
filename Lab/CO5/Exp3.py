import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Python is a programming language.",
    "Artificial intelligence makes machines intelligent.",
    "Machine learning learns from data.",
    "Generative AI creates new content."
]

embeddings = model.encode(documents)

vectors = np.array(embeddings, dtype='float32')

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

query = input("Enter search query: ")

q = model.encode([query])
q = np.array(q, dtype='float32')

distances, indices = index.search(q, 2)

print("\nRetrieved Documents:")

for i in indices[0]:
    print(documents[i])