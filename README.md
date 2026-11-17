# SkillBridge AI – Prototype 0.1

A beginner-friendly Flask web application starter for the SkillBridge AI Ideathon project.

## Requirements
- Python 3.10 or newer
- VS Code
- Internet connection for installing Flask

## Run on Windows
1. Extract this folder.
2. Open the `skillbridge_ai` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:

   ```powershell
   py -m venv venv
   ```

5. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:

   ```cmd
   venv\Scripts\activate.bat
   ```

6. Install Flask:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the app:

   ```powershell
   python app.py
   ```

8. Open the local address shown in the terminal, usually `http://127.0.0.1:5000`.

## Current functionality
- Landing page
- Student profile form
- Flask receives form data and displays a profile summary

## Next modules
1. Career Path Predictor
2. Skill Gap Analyzer
3. Career Readiness Simulator
4. Learning roadmap and persistent database

Note: This first version does not yet save profiles permanently and does not make real AI predictions. Those will be added in later modules.
