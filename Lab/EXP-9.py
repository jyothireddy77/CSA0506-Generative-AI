from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

text = "Artificial Intelligence is"

result = generator(text, max_new_tokens=30, do_sample=False)

print(result[0]["generated_text"])