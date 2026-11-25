from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

documents = [
    Document(page_content="Python is a programming language."),
    Document(page_content="Machine learning learns from data."),
    Document(page_content="AI makes machines intelligent."),
    Document(page_content="Generative AI creates new content.")
]

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents,
    embeddings,
    collection_name="context_data"
)

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

llm = HuggingFacePipeline(pipeline=generator)

history = ""

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=2)

    context = " ".join([d.page_content for d in docs])

    prompt = (
        "Previous conversation: " + history +
        " Context: " + context +
        " Question: " + question
    )

    answer = llm.invoke(prompt)

    print("Bot:", answer)

    history += " User: " + question + " Bot: " + answer