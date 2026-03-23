from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
API_KEY = os.getenv("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")

print("API KEY:", API_KEY)  # DEBUG

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "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"

@app.get("/")
def home():
    return {"message": "NEXORA AI FREE running 🚀"}

@app.get("/chat")
def chat(user_input: str):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                # ✅ FINAL WORKING MODEL
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional business chatbot. Ask for name and phone if user is interested."
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )

        data = response.json()
        print("DEBUG:", data)

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
        else:
            reply = "Error: " + str(data)

        return {"message": reply}

    except Exception as e:
        return {"error": str(e)}
