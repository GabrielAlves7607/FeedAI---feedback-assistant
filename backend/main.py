from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import Feedback, SessionLocal, init_db
from classifier import classify_feedback
from proxy import router as proxy_router
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Configure CORS (adjust allowed origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the database
init_db()

# HTML template directory
templates = Jinja2Templates(directory="templates")

# Pydantic input model for feedback
class FeedbackIn(BaseModel):
    message: str
    branch: str

# Endpoint to submit a new feedback
@app.post("/submit/")
def submit_feedback(feedback: FeedbackIn):
    # Classify the feedback message (compliment, complaint, or neutral)
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

# Endpoint to list all feedbacks (JSON)
@app.get("/feedbacks/")
def get_all_feedbacks():
    db = SessionLocal()
    try:
        feedbacks = db.query(Feedback).all()
        return feedbacks
    finally:
        db.close()

# Endpoint for the main HTML page (/)
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

# Include Verbeux API proxy routes
app.include_router(proxy_router)
