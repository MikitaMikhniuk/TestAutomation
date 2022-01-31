@echo off
python3 --version > NUL 2>&1
if ERRORLEVEL 1 echo "No Python3 distributable! PLease isntall Python3 to proceed." & exit 1

pip install --upgrade pip
python3 -m venv env
env\Scripts\pip install pytest
env\Scripts\python -m pytest tests/pen_test.py > results.txt
