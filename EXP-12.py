import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

sentence = "Machine learning is powerful"

inputs = tokenizer(sentence, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

embeddings = outputs.last_hidden_state

print("Contextual Embeddings Shape:", embeddings.shape)
print("Embeddings:", embeddings)