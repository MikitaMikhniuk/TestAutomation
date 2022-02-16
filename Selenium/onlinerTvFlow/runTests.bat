@echo off
python3 --version > NUL 2>&1
if ERRORLEVEL 1 echo "No Python3 distributable! PLease isntall Python3 to proceed." & exit 1

pip install --upgrade pip
python3 -m venv test_env
test_env\Scripts\pip install pytest
test_env\Scripts\pip install selenium
test_env\Scripts\pip install webdriver_manager
test_env\Scripts\pip install pytest-html
test_env\Scripts\pip install pytest-repeat  
test_env\Scripts\python -m pytest --html=results.html --self-contained-html --count=10
