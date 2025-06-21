from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

router = APIRouter()

# Verbeux API credentials
API_KEY = "YOUR_API_KEY_HERE"
ASSISTANT_ID = "YOUR_ASSISTANT_ID_HERE"

# Pydantic model for incoming chat messages
class Message(BaseModel):
    message: str

# Proxy endpoint to forward chat messages to Verbeux Generative API
@router.post("/chat")
def chat(msg: Message):
    url = f"https://generative-api.verbeux.com.br/v1/assistants/{ASSISTANT_ID}/completion"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "input": {
            "text": msg.message
        }
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return {"error": f"HTTP Error: {errh}"}
    except requests.exceptions.ConnectionError as errc:
        return {"error": f"Connection Error: {errc}"}
    except requests.exceptions.Timeout as errt:
        return {"error": f"Timeout Error: {errt}"}
    except requests.exceptions.RequestException as err:
        return {"error": f"Unexpected Error: {err}"}
