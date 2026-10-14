from transformers import pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

text = "This movie is excellent"

result = sentiment(text)

print("Sentiment:", result)