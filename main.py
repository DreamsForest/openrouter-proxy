from fastapi import FastAPI, Request
import requests

app = FastAPI()


OPENROUTER_API_KEY = "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"

@app.post("/proxy")
async def proxy(request: Request):
    body = await request.json()

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://your-app.com",
        "X-Title": "Math Tutor App"
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=body,
        timeout=60
    )

    return response.json()
