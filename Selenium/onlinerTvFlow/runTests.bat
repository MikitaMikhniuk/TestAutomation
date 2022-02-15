@echo off
python3 --version > NUL 2>&1
if ERRORLEVEL 1 echo "No Python3 distributable! PLease isntall Python3 to proceed." & exit 1

pip install --upgrade pip
python3 -m venv selen_env
selen_env\Scripts\pip install pytest
selen_env\Scripts\pip install selenium
selen_env\Scripts\pip install pytest-html
selen_env\Scripts\python -m pytest tests/_test.py --html=results.html --self-contained-html > results.html
