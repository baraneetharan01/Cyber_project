# 🚀 Quick Run Guide

## One-Time Setup

**PowerShell:**
```powershell
.\setup.ps1
```

**CMD/Batch:**
```bash
.\setup.bat
```

## Run the Application

**PowerShell:**
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

## Access
- **Web UI**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## If You Get Errors

### "ModuleNotFoundError"
→ Run: `setup.bat` (installs dependencies)

### "Model not found"
→ Train model: `python -m src.training.train --config configs/config.yaml`

### "Port 8000 in use"
→ Close other apps or change port in `run.py`

---

## Full Documentation
- **Setup Guide**: `SETUP_GUIDE.md`
- **Detailed Run Guide**: `HOW_TO_RUN.md`
- **Main README**: `README.md`

