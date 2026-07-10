from rag import retrieve_context

question = "How can I reduce plastic use at home?"

context = retrieve_context(question)

print("Retrieved Context:\n")
print(context)