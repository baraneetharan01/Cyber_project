import os
from typing import Dict, Any
import joblib
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

MODEL_PATH = os.environ.get("MODEL_PATH", "models/model.pkl")
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static")

app = FastAPI(title="Threat Detection System", version="1.0.0")

# API router under /api so we can serve static UI at root
api = APIRouter(prefix="/api")


def _load_model():
    """Load the trained model from disk."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train the model first.")
    return joblib.load(MODEL_PATH)


@api.get("/health")
def health() -> Dict[str, Any]:
    """Health check endpoint."""
    return {"status": "ok"}


@api.get("/model/info")
def model_info() -> Dict[str, Any]:
    """Get model information."""
    model_exists = os.path.exists(MODEL_PATH)
    return {
        "status": "loaded" if model_exists else "not_found",
        "model_path": MODEL_PATH,
        "exists": model_exists
    }


@api.post("/predict")
def predict(features: Dict[str, Any]) -> Dict[str, Any]:
    """Predict threat from feature values."""
    try:
        model = _load_model()
        # Expect a single record as JSON dictionary
        import pandas as pd
        X = pd.DataFrame([features])
        
        # The model is a pipeline, so predict directly
        preds = model.predict(X)
        prediction = preds[0]
        
        # Get confidence if available
        if hasattr(model, "predict_proba"):
            probas = model.predict_proba(X)
            max_proba = float(probas.max(axis=1)[0])
        else:
            max_proba = None
        
        return {
            "prediction": str(prediction),
            "confidence": max_proba,
            "input": features
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=f"Model not available: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")


# Register API router
app.include_router(api)

# Serve static files under /static and index at /
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"detail": "Not Found"}


