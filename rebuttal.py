# from simplify import simplifyit
# from read_pdf import read_pdf_file
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# # openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure this env var is set

# api = os.getenv("OPENAI_API_KEY")
# client = openai.OpenAI(
#     api_key=api,
#     base_url="https://openrouter.ai/api/v1",
# )

# def generate_rebuttal_from_pdf(pdf_text, reason):
#     simplified = simplifyit(pdf_text)
#     prompt = f"""
#     You are a professional insurance expert. Given the following insurance policy:

#     {simplified}

#     And the claim was denied for this reason:
#     "{reason}"
#     Your task is to write a direct , clear and firm Rebuttal that cites relevant policy terms and argues for reconsideration.
#     The rebuttal argues why the denial was invalid and is up for reconsideration
#     Keep your response short yet perfect as a rebuttal
#     Return your response in **Markdown Format**
#     """
#     try:
#         response = client.chat.completions.create(
#             model="mistralai/mistral-7b-instruct", messages=[
#                 {"role": "system", "content": "You are a helpful insurance expert."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         reply = response.choices[0].message.content.strip()
#         return {"rebuttal": reply}  # Simple logic
#     except Exception as e:
#         return {"error": f"OpenAI failed: {str(e)}"}

# def generate_rebuttal_from_text(reason):
#     prompt = f"""
#     You are an insurance expert. A user explained the following situation:
#     "{reason}"
    
#     Write a strong and professional rebuttal that challenges the denial with sound reasoning.
#     """
#     try:
#         response = client.chat.completions.create(
#             model="mistralai/mistral-7b-instruct", messages=[
#                 {"role": "system", "content": "You are a professional claims advocate."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         reply = response.choices[0].message.content.strip()
#         return {"rebuttal": reply, "matched_clauses": []}
#     except Exception as e:
#         return {"error": f"OpenAI error: {str(e)}"}





import os
import requests
from dotenv import load_dotenv
from simplify import simplifyit
from read_pdf import read_pdf_file

# Load API key from .env
load_dotenv()
api = os.getenv("OPENAI_API_KEY")

if not api:
    raise ValueError("API_KEY not found in .env file")

# Common function to call OpenRouter API
def call_openrouter(prompt, system_message="You are a helpful insurance expert."):
    headers = {
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://policy-mate-frontend.vercel.app",  # Replace with your actual project URL
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ OpenRouter API error: {str(e)}"

# Generate rebuttal from PDF text and reason
def generate_rebuttal_from_pdf(pdf_text, reason):
    simplified = simplifyit(pdf_text)

    prompt = f"""
You are a professional insurance expert. Given the following insurance policy:

{simplified}

And the claim was denied for this reason:
"{reason}"

Your task is to write a direct, clear, and firm rebuttal that cites relevant policy terms and argues for reconsideration.

The rebuttal should argue why the denial was invalid and should be reconsidered.

Return the response in **Markdown format**.
"""
    reply = call_openrouter(prompt)
    return {"rebuttal": reply}

# Generate rebuttal from plain text
def generate_rebuttal_from_text(reason):
    prompt = f"""
You are an insurance expert. A user explained the following situation:
"{reason}"

Write a strong and professional rebuttal that challenges the denial with sound reasoning.

Respond in **Markdown format**.
"""
    reply = call_openrouter(prompt, system_message="You are a professional claims advocate.")
    return {"rebuttal": reply, "matched_clauses": []}
