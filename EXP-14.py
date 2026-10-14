from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="distilbert/distilbert-base-cased-distilled-squad"
)

context = "Python is a popular programming language used in Artificial Intelligence."

question = "Which programming language is used in Artificial Intelligence?"

result = qa(question=question, context=context)

print("Answer:", result["answer"])