
    
    
# import os
# import requests
# from dotenv import load_dotenv
# from simplify import simplifyit
# from read_pdf import read_pdf_file

# # Load OpenRouter API key
# load_dotenv()
# api = os.getenv("OPENAI_API_KEY")

# if not api:
#     raise ValueError("API_KEY not found in .env file")

# def verify_from_pdf(pdf_text, claim):
#     simplified = simplifyit(pdf_text)

#     prompt = (
#         "You are an insurance compliance assistant.\n\n"
#         "Compare the following:\n\n"
#         f"🧾 **Agent Explanation:**\n{claim}\n\n"
#         f"📄 **Policy Document Summary:**\n{simplified}\n\n"
#         "**Your Task:**\n"
#         "- Identify if the agent explanation contains any misleading claims.\n"
#         "- Point out any missing or contradictory information.\n"
#         "- If the explanation is accurate and complete, state that clearly.\n\n"
#         "Respond in **Markdown format**. Be short, direct, and easy to understand."
#     )

#     headers = {
#         "Authorization": f"Bearer {api}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://policy-mate-frontend.vercel.app",  # Replace with your deployed frontend URL
#     }

#     data = {
#         "model": "mistralai/mistral-7b-instruct",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are a helpful and the best insurance expert."
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         "temperature": 0.6,
#         "max_tokens": 800
#     }

#     try:
#         response = requests.post("https://openrouter.ai/api/v1", headers=headers, json=data)
#         response.raise_for_status()
#         result = response.json()
#         return {'verify': result["choices"][0]["message"]["content"].strip()}
#     except Exception as e:
#         return {"error": f"❌ OpenRouter error: {str(e)}"}

import os
import requests
from dotenv import load_dotenv
from simplify import simplifyit
from read_pdf import read_pdf_file

# Load OpenRouter API key
load_dotenv()
api = os.getenv("OPENAI_API_KEY")

if not api:
    raise ValueError("API_KEY not found in .env file")

def verify_from_pdf(pdf_text, claim):
    simplified = simplifyit(pdf_text)

    prompt = (
        "You are an insurance compliance assistant.\n\n"
        "Compare the following:\n\n"
        f"🧾 **Agent Explanation:**\n{claim}\n\n"
        f"📄 **Policy Document Summary:**\n{simplified}\n\n"
        "**Your Task:**\n"
        "- Identify if the agent explanation contains any misleading claims.\n"
        "- Point out any missing or contradictory information.\n"
        "- If the explanation is accurate and complete, state that clearly.\n\n"
        "Respond in **Markdown format**. Be short, direct, and easy to understand."
    )

    headers = {
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://policy-mate-frontend.vercel.app",  # Replace with your actual frontend URL
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",  # You can use other supported models as well
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful and the best insurance expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.6,
        "max_tokens": 800
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",  # ✅ Correct endpoint
            headers=headers,
            json=data
        )
        response.raise_for_status()

        result = response.json()
        return {'verify': result["choices"][0]["message"]["content"].strip()}

    except requests.exceptions.RequestException as e:
        # Log raw response if available
        try:
            return {"error": f"❌ OpenRouter HTTP error: {e.response.text}"}
        except:
            return {"error": f"❌ OpenRouter request failed: {str(e)}"}
    except ValueError as e:
        return {"error": f"❌ JSON parsing error: {str(e)}"}
