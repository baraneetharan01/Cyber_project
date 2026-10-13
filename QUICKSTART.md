# Quick Start Guide

## Single Command to Run Everything

After training the model, simply run:

**Windows:**
```bash
run.bat
```

**Or:**
```bash
python run.py
```

**Linux/Mac:**
```bash
python3 run.py
```

## What Happens

1. Server starts on **http://localhost:8000**
2. Open your browser to **http://localhost:8000**
3. You'll see the Threat Detection UI
4. Use the UI to:
   - Check API health
   - Enter feature values as JSON
   - Get threat predictions

## Example JSON Input

```json
{
  "feature1": 12,
  "feature2": 0.15,
  "protocol": "TCP"
}
```

## All Features in One Place

- **Frontend UI**: http://localhost:8000
- **API Endpoints**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Predict**: POST to http://localhost:8000/predict

No separate terminals needed! Everything runs together.

