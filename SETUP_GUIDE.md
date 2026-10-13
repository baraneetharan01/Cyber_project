# Setup and Run Guide - Threat Detection System

## Prerequisites
- Python 3.8 or higher (you have Python 3.13.3 ✓)
- pip (Python package manager)

## Step-by-Step Setup

### 1. Create Virtual Environment (Recommended)

**Option 1: Use Setup Script (Recommended)**

**PowerShell:**
```powershell
.\setup.ps1
```

**CMD/Batch:**
```bash
.\setup.bat
```

**Option 2: Manual Setup**

**Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows CMD:**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

**Note:** If you get an execution policy error in PowerShell, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

This will install:
- pandas, numpy, scikit-learn
- fastapi, uvicorn
- pyyaml, joblib

### 3. Verify Model Exists

Make sure you have a trained model:
```bash
# Check if model exists
dir models\model.pkl
```

If the model doesn't exist, train it first:
```bash
python -m src.training.train --config configs/config.yaml
```

### 4. Run the Application

**PowerShell (Recommended):**
```powershell
.\run.ps1
```

**CMD/Batch:**
```bash
.\run.bat
```

**Or directly:**
```bash
python run.py
```

### 5. Access the Application

Once running, open your browser:
- **Frontend UI**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Error: "Model not found at models/model.pkl"
**Solution:** Train the model first:
```bash
python -m src.training.train --config configs/config.yaml
```

### Error: "Execution policy" in PowerShell
**Solution:** Run this command:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: Port 8000 already in use
**Solution:** Either:
1. Stop the application using port 8000
2. Or modify `run.py` to use a different port

### Error: "Target column 'label' not found"
**Solution:** Check your `data/raw/dataset.csv` has a column named `label`

## Quick Test

After setup, test the API:
```bash
# Health check
curl http://localhost:8000/api/health

# Or in PowerShell:
Invoke-WebRequest -Uri http://localhost:8000/api/health
```

## Example Prediction

Use the web UI at http://localhost:8000 or send a POST request:

```json
POST http://localhost:8000/api/predict
Content-Type: application/json

{
  "feature1": 12,
  "feature2": 0.15,
  "protocol": "TCP"
}
```

## Project Structure

```
├── src/              # Source code
├── data/             # Data files
├── models/           # Trained models
├── configs/          # Configuration files
├── static/           # Frontend HTML
├── reports/          # Evaluation metrics
├── requirements.txt  # Python dependencies
└── run.py           # Main entry point
```

