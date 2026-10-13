# Threat Detection System - PowerShell Run Script
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Threat Detection System" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run .\setup.bat first to create and configure the environment." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if model exists
if (-not (Test-Path "models\model.pkl")) {
    Write-Host "WARNING: Model file not found at models\model.pkl" -ForegroundColor Yellow
    Write-Host "You may need to train the model first:" -ForegroundColor Yellow
    Write-Host "  python -m src.training.train --config configs\config.yaml" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y" -and $continue -ne "Y") {
        exit 1
    }
}

Write-Host "Starting server on http://localhost:8000" -ForegroundColor Green
Write-Host "Frontend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press CTRL+C to stop" -ForegroundColor Yellow
Write-Host ""

# Activate virtual environment and run
& .venv\Scripts\python.exe run.py
