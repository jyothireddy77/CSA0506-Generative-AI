from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = "Natural Language Processing is useful"

tokens = tokenizer.tokenize(sentence)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Sentence:", sentence)
print("Tokens:", tokens)
print("Token IDs:", token_ids)