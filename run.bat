@echo off
echo ============================================================
echo Threat Detection System
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first to create and configure the environment.
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if model exists
if not exist "models\model.pkl" (
    echo WARNING: Model file not found at models\model.pkl
    echo You may need to train the model first:
    echo   python -m src.training.train --config configs\config.yaml
    echo.
    echo Continue anyway? (y/n)
    set /p continue=
    if /i not "%continue%"=="y" exit /b 1
)

echo Starting server on http://localhost:8000
echo Frontend: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo Press CTRL+C to stop
echo.

python run.py
pause
