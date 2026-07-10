from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load the same embedding model used during indexing
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load the saved FAISS vector database
vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

def retrieve_context(question):
    """
    Search the vector database and return the most relevant document chunks.
    """

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context