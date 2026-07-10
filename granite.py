from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

from config import IBM_API_KEY, IBM_PROJECT_ID, IBM_URL

credentials = Credentials(
    url=IBM_URL,
    api_key=IBM_API_KEY
)

parameters = {
    "max_new_tokens": 350,
    "temperature": 0.3,
    "top_p": 0.9
}

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=IBM_PROJECT_ID,
    params=parameters
)

def ask_granite(question, context):

    print("\n========== CONTEXT SENT TO GRANITE ==========\n")
    print(context[:1500])   # print first 1500 characters
    print("\n=============================================\n")

    prompt = f"""
You are an Eco Lifestyle Assistant.

Use ONLY the information provided below to answer the question.

If the answer is not available in the context, reply:
"I couldn't find that information in my knowledge base."

Context:
{context}

Question:
{question}

Provide:
- A clear explanation
- Practical suggestions
- Bullet points where appropriate
"""

    return model.generate_text(prompt=prompt)