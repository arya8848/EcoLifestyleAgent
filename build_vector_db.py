import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Folder containing your PDFs
DATA_PATH = "data"

# Folder where the vector database will be saved
VECTOR_DB_PATH = "vector_db"

print("Loading PDF documents...")

loader = PyPDFDirectoryLoader(DATA_PATH)
documents = loader.load()

print(f"Loaded {len(documents)} pages.")

print("Splitting documents into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} text chunks.")

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS vector database...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local(VECTOR_DB_PATH)

print("✅ Vector database created successfully!")