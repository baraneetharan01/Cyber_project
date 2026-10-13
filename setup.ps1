# Threat Detection System - PowerShell Setup Script
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Threat Detection System - Setup Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "Virtual environment created." -ForegroundColor Green
    Write-Host ""
}

# Activate virtual environment and install dependencies
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .venv\Scripts\python.exe -m pip install --upgrade pip | Out-Null

Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
& .venv\Scripts\python.exe -m pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "Setup complete!" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Make sure you have a trained model: models\model.pkl" -ForegroundColor White
    Write-Host "   If not, run: python -m src.training.train --config configs\config.yaml" -ForegroundColor Gray
    Write-Host ""
    Write-Host "2. Run the application:" -ForegroundColor White
    Write-Host "   .\run.ps1" -ForegroundColor Gray
    Write-Host "   OR" -ForegroundColor Gray
    Write-Host "   .\run.bat" -ForegroundColor Gray
    Write-Host "   OR" -ForegroundColor Gray
    Write-Host "   python run.py" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Read-Host "Press Enter to exit"

