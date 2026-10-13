# How to Run the Project Without Errors

## Quick Start (3 Steps)

### Step 1: Setup (First Time Only)
Run the setup script to install dependencies:

**PowerShell:**
```powershell
.\setup.ps1
```

**CMD/Batch:**
```bash
.\setup.bat
```

Or manually:
```bash
# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Verify Model Exists
Check if you have a trained model:
```bash
dir models\model.pkl
```

If the model doesn't exist, train it:
```bash
python -m src.training.train --config configs\config.yaml
```

### Step 3: Run the Application

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

## Common Errors and Solutions

### ❌ Error: "ModuleNotFoundError: No module named 'fastapi'"
**Cause:** Dependencies not installed or wrong Python environment

**Solution:**
```powershell
# Run setup script
.\setup.ps1

# Or manually activate and install
.venv\Scripts\activate
pip install -r requirements.txt
```

### ❌ Error: "Model not found at models/model.pkl"
**Cause:** Model hasn't been trained yet

**Solution:**
```bash
python -m src.training.train --config configs/config.yaml
```

### ❌ Error: "Execution policy" in PowerShell
**Cause:** PowerShell script execution is restricted

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ Error: "Port 8000 already in use"
**Cause:** Another application is using port 8000

**Solution:**
1. Close the other application
2. Or modify `run.py` line 27 to use a different port (e.g., `port=8001`)

### ❌ Error: "Target column 'label' not found"
**Cause:** Dataset doesn't have the expected column name

**Solution:**
1. Check `data/raw/dataset.csv` has a column named `label`
2. Or update `configs/config.yaml` to match your dataset's target column name

## Verification Checklist

Before running, verify:

- [ ] Virtual environment exists (`.venv` folder)
- [ ] Dependencies installed (`pip list` shows fastapi, uvicorn, etc.)
- [ ] Model file exists (`models/model.pkl`)
- [ ] Dataset exists (`data/raw/dataset.csv`)
- [ ] Config file exists (`configs/config.yaml`)

## Testing the Application

1. **Start the server:**
   ```powershell
   .\run.ps1
   ```
   Or:
   ```bash
   .\run.bat
   ```

2. **Open browser:** http://localhost:8000

3. **Test health endpoint:**
   ```powershell
   Invoke-WebRequest -Uri http://localhost:8000/api/health
   ```

4. **Test prediction:**
   - Use the web UI at http://localhost:8000
   - Or send POST request to http://localhost:8000/api/predict

## Using Virtual Environment

Always activate the virtual environment before running:

```bash
# Activate
.venv\Scripts\activate

# Now run commands
python run.py

# Deactivate when done
deactivate
```

## Alternative: Direct Python (Not Recommended)

If you don't want to use virtual environment:
```bash
pip install -r requirements.txt
python run.py
```

**Note:** This installs packages globally, which can cause conflicts with other projects.

## Project Status

✅ **Ready to run if:**
- Virtual environment is set up
- Dependencies are installed
- Model is trained

The project is configured correctly and should run without errors if the above conditions are met!

