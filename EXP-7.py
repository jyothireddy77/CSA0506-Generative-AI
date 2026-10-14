from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = "I love learning Artificial Intelligence"

result = classifier(text)

print(result)