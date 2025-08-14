@echo off
cd /d "C:\liv-analyser-vk-deployment"

rem activate virtual environment
call .venv\Scripts\activate.bat

rem run python script and keep window open
:loop
python liv_analyser_vk\analyser.py
echo Script stopped unexpectedly. Restarting in 5 seconds...
timeout /t 5
goto loop