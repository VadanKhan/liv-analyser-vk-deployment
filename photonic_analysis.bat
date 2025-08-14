@echo off
cd /d "C:\liv-analyser-vk-deployment"
start /min cmd /c ".venv\Scripts\activate.bat && python liv_analyser_vk\analyser.py"