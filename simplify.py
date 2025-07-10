

import os
import requests
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("OPENAI_API_KEY")

if not api:
    raise ValueError("API_KEY not found in .env file")

def simplifyit(text):
    prompt = f"""
Here is an insurance policy document:

\"\"\"{text}\"\"\"

Your task is to analyze the document and create a short, direct, clear, and concise summary of it.
- Your response should be in **bullet points**.
- Use **abstractive summarization**.
- Format the result in **Markdown**.
"""

    headers = {
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://policy-mate-frontend.vercel.app",  # Replace this with your frontend URL or GitHub repo
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # or any other supported model
        "messages": [
            {"role": "system", "content": "You are a helpful insurance explainer."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 1000
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error simplifying policy: {e}"
