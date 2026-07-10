from rag import retrieve_context
from granite import ask_granite

question = "What are the responsibilities for plastic waste management?"

context = retrieve_context(question)

answer = ask_granite(question, context)

print("\n========== FINAL ANSWER ==========\n")
print(answer)