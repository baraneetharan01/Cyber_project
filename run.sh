#!/bin/bash
echo "Starting Threat Detection System..."
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""

# Start backend in background
source .venv/bin/activate
python -m uvicorn src.serving.app:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Start frontend
cd frontend
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo "Starting frontend..."
npm run dev

# Cleanup: Kill backend when script exits
kill $BACKEND_PID 2>/dev/null

