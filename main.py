from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")

@app.post("/proxy")
async def proxy(request: Request):
    try:
        body = await request.json()

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://example.com",   # ← тут можно твой сайт
            "X-Title": "Math Tutor App"              # ← любое название
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=60
        )

        return response.json()
    except Exception as e:
        return {"error": str(e)}
