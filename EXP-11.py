from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = "I am studying machine learning"

encoded = tokenizer(sentence)

print("Input IDs:", encoded["input_ids"])
print("Attention Mask:", encoded["attention_mask"])