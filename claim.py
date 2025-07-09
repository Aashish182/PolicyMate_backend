# import os
# import openai
# from dotenv import load_dotenv 

# load_dotenv()
# api=os.getenv("OPENAI_API_KEY")
# client = openai.OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=api,
# )
# # print(api)

# def explain_claim_denial(treatment, reason, policy_type):
#     prompt = f"""
# You are a friendly insurance assistant.

# A claim was denied.

# Policy Type: {policy_type}
# Treatment: {treatment}
# Rejection Reason: {reason}

# Now do 2 things:
# 1. Write a simple, polite explanation of why the claim was denied.
# 2. Write a friendly counterpoint the customer can include in an appeal.
# """


#     try:
#         response = client.chat.completions.create(
#             model="mistralai/mistral-7b-instruct:free",
#             messages=[
#                 {"role": "system", "content": "You are an empathetic insurance assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )

#         return response.choices[0].message.content

#     except Exception as e:
#         return f"❌ OpenRouter error: {str(e)}"



import os
import requests
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api = os.getenv("OPENAI_API_KEY")

if not api:
    raise ValueError("API_KEY not found in .env file")

def explain_claim_denial(treatment, reason, policy_type):
    prompt = f"""
You are a friendly insurance assistant.

A claim was denied.

📄 **Policy Type**: {policy_type}  
💉 **Treatment**: {treatment}  
❌ **Rejection Reason**: {reason}  

Now do 2 things:
1. Write a simple, polite explanation of why the claim was denied.
2. Write a friendly counterpoint the customer can include in an appeal.

Return the answer in **Markdown format**.
"""

    headers = {
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-project-url.com",  # Replace with your actual domain or GitHub repo
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # You used ":free" but that may not be necessary
        "messages": [
            {"role": "system", "content": "You are an empathetic insurance assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ OpenRouter error: {str(e)}"
