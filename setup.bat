@echo off
echo ============================================================
echo Threat Detection System - Setup Script
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================================
echo Setup complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Make sure you have a trained model: models\model.pkl
echo    If not, run: python -m src.training.train --config configs\config.yaml
echo.
echo 2. Run the application:
echo    run.bat
echo    OR
echo    python run.py
echo.
pause

