# 🛡️ ClearClaim – AI-Powered Insurance Assistant

ClearClaim is a powerful web platform that helps users **understand their insurance policies**, **verify what agents say**, and **generate professional rebuttals** for denied claims — all with the help of AI.

---

## ❓ Problem Statement

- 🧾 Insurance documents are complex and filled with legal jargon.  
- ❌ Claim rejections are often vague or unexplained.  
- 🤷‍♂️ Users have no guidance on how to appeal or verify claim information.

---

## ✅ Our Solution

- 🔍 **Simplifies insurance policy PDFs** into easy-to-read summaries.  
- 🧠 **Verifies if an agent's claim is aligned** with your actual policy terms.  
- ✉️ **Generates strong, professional rebuttals** to challenge unfair denials.

---

## 🚀 Features

- ✅ Simplify Insurance Policy Documents (PDFs)  
- ✅ Generate AI-Powered Rebuttals for Rejected Claims  
- ✅ Verify Agent's Explanation Against Actual Policy  



## 🛠️ Setup Instructions

### 🔧 Backend (Python + Flask)

```bash
cd backend
pip install -r requirements.txt
```

1. Create a `.env` file with:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
2. Run the server:
   ```bash
   python app.py
   ```

---

Hosted via Render — remember to configure the environment variables (`OPENAI_API_KEY`) via the Render dashboard and restart the service after updates.


## 🧠 AI & NLP

- 🤖 Model: `mistralai/mistral-7b-instruct` (via OpenRouter)  
- 📋 Prompt-engineered NLP logic for summarization, verification, rebuttal generation  
- 📄 Intelligent extraction of clauses, exclusions, and conditions

---


## 📌 Roadmap

- [x] PDF Policy Simplifier  
- [x] AI Rebuttal Generator  
- [x] Agent Claim Verifier    

---

## 🧪 Tech Stack

- ⚙️ Flask + Python (Backend)  
- ⚛️ React + Axios (Frontend)  
- 📦 PyPDF2, dotenv, OpenAI SDK  
- 🌐 OpenRouter (LLM API Layer)

---

## 📃 License

MIT License

---

## 👨‍💻 Author

Made by **Aashish Gupta**
