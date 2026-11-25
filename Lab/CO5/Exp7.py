from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

documents = [
    Document(page_content="Water distribution supplies water to different areas."),
    Document(page_content="Pipelines transport water to consumers."),
    Document(page_content="Leak detection identifies damaged pipelines."),
    Document(page_content="Sensors monitor water flow and pressure.")
]

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents,
    embeddings,
    collection_name="water_knowledge"
)

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

llm = HuggingFacePipeline(pipeline=generator)

question = input("Ask a question: ")

docs = db.similarity_search(question, k=2)

context = " ".join([d.page_content for d in docs])

prompt = "Answer using this information: " + context + " Question: " + question

print("\nChatbot:", llm.invoke(prompt))