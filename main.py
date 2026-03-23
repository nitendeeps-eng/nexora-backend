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
    return {"message": "NEXORA AI running 🚀"}

@app.get("/chat")
def chat(user_input: str):
    try:
        response = requests.post(
            "https://router.huggingface.co/hf-inference/models/google/flan-t5-large",
            headers={
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "inputs": user_input
            }
        )

        data = response.json()
        print("DEBUG:", data)

        if isinstance(data, list):
            reply = data[0]["generated_text"]
        else:
            reply = str(data)

        return {"message": reply}

    except Exception as e:
        return {"error": str(e)}
