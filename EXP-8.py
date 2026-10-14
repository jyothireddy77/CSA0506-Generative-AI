from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = "Artificial Intelligence is interesting"

tokens = tokenizer.tokenize(sentence)

print("Tokens:", tokens)