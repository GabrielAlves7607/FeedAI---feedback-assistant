from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import Feedback, SessionLocal, init_db
from classifier import classify_feedback
from proxy import router as proxy_router
from fastapi.middleware.cors import CORSMiddleware

# Inicializa a aplicação FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou ajuste para o domínio do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura os arquivos estátivos 
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inicializa o banco de dados
init_db()

# Define o diretório dos templates HTML
templates = Jinja2Templates(directory="templates")

# Modelo de entrada dos dados (pydantic)
class FeedbackIn(BaseModel):
    message: str
    branch: str


# Endpoint para criar um novo feedback
@app.post("/submit/")
def submit_feedback(feedback: FeedbackIn):
    # Classifica a mensagem (compliment, complaint ou neutral)
    classification = classify_feedback(feedback.message)
    db = SessionLocal()
    try:
        entry = Feedback(
            message=feedback.message,
            branch=feedback.branch,
            feedback_type=classification
        )
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return {
            "id": entry.id,
            "type": classification,
            "message": entry.message,
            "branch": entry.branch
        }
    finally:
        db.close()


# Endpoint para listar todos os feedbacks (JSON)
@app.get("/feedbacks/")
def get_all_feedbacks():
    db = SessionLocal()
    try:
        feedbacks = db.query(Feedback).all()
        return feedbacks
    finally:
        db.close()


# Endpoint da página web principal (/)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    db = SessionLocal()
    try:
        feedbacks = db.query(Feedback).all()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "feedbacks": feedbacks
        })
    finally:
        db.close()

# Incluindo as rotas do proxy
app.include_router(proxy_router)
