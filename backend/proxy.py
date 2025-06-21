from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()
router = APIRouter()

# Suas credenciais da API Verbeux
API_KEY = "a453729a-4978-49c3-926e-ea59c6e25412"
ASSISTANT_ID = 806


# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para a mensagem
class Message(BaseModel):
    message: str

# Endpoint de proxy
@router.post("/chat")
def chat(msg: Message):
    url = f"generative-api.verbeux.com.br/session/{ASSISTANT_ID}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "input": {
            "message": msg.message,
            "assistant_id": 806
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
        return {"error": f"Something went wrong: {err}"}

# Incluindo as rotas no app
app.include_router(router)
