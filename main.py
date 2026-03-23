from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("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")

@app.get("/")
def home():
    return {"message": "NEXORA AI (Groq) running 🚀"}

@app.get("/chat")
def chat(user_input: str):
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a business chatbot. Ask for name and phone if user is interested."},
                    {"role": "user", "content": user_input}
                ]
            }
        )

        data = response.json()
        print("DEBUG:", data)

        # ✅ SAFE HANDLING
        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
        else:
            reply = "Error: " + str(data)

        return {"message": reply}

    except Exception as e:
        return {"error": str(e)}
