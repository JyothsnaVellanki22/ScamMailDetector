from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
import string

app = FastAPI(title="Spam Detector API")

# Configure CORS
origins = [
    "http://localhost:4200",  # Angular default port
    "http://localhost:3000",  # React default port (just in case)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../models/spam_classifier.joblib")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model not found at {MODEL_PATH}. Please run src/train.py first.")

model = joblib.load(MODEL_PATH)

class MessageRequest(BaseModel):
    message: str

class PredictionResponse(BaseModel):
    label: str
    confidence: float
    is_spam: bool

def preprocess_text(text: str) -> str:
    """
    Same preprocessing as used in training.
    """
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

@app.get("/")
def read_root():
    return {"message": "Spam Detector API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict_spam(request: MessageRequest):
    try:
        clean_msg = preprocess_text(request.message)
        
        # Predict
        prediction = model.predict([clean_msg])[0]
        proba = model.predict_proba([clean_msg])[0]
        confidence = float(max(proba))
        
        is_spam = (prediction == 'spam')
        
        return PredictionResponse(
            label=prediction,
            confidence=confidence,
            is_spam=is_spam
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
