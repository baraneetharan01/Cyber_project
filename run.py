#!/usr/bin/env python
"""
Simple script to run the Threat Detection System.
Starts the FastAPI server on port 8000.
"""
import uvicorn
import os
import sys

if __name__ == "__main__":
    # Ensure we're in the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if we're in a virtual environment, if not, try to use .venv
    venv_python = os.path.join(script_dir, ".venv", "Scripts", "python.exe")
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        # Not in a virtual environment
        if os.path.exists(venv_python):
            print("=" * 60)
            print("WARNING: Not using virtual environment!")
            print("=" * 60)
            print(f"\nPlease use the virtual environment's Python:")
            print(f"  {venv_python} run.py")
            print("\nOr use the run scripts:")
            print("  .\\run.ps1  (PowerShell)")
            print("  .\\run.bat  (CMD)")
            print("\nAttempting to continue anyway...\n")
    
    print("=" * 60)
    print("Threat Detection System")
    print("=" * 60)
    print("\nStarting server on http://localhost:8000")
    print("Frontend: http://localhost:8000")
    print("API Docs: http://localhost:8000/docs")
    print("\nPress CTRL+C to stop\n")
    
    try:
        uvicorn.run(
            "src.serving.app:app",
            host="0.0.0.0",
            port=8000,
            reload=False,  # Set to True for development
        )
    except ModuleNotFoundError as e:
        print("\n" + "=" * 60)
        print("ERROR: Missing dependencies!")
        print("=" * 60)
        print(f"\n{str(e)}")
        print("\nPlease install dependencies:")
        print("  .\\setup.ps1  (PowerShell)")
        print("  .\\setup.bat  (CMD)")
        print("\nOr manually:")
        print("  .venv\\Scripts\\activate")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        sys.exit(0)

