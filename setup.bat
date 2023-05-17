@echo off

REM Check Python is installed
python --version
if errorlevel 1 (
    echo Python not found.
    exit /b 1
)

REM Install Poetry
python -m pip install poetry
if errorlevel 1 (
    echo Poetry installation failed.
    exit /b 1
)

REM Run Poetry install --sync
python -m poetry install --sync
if errorlevel 1 (
    echo "poetry install --sync failed."
    exit /b 1
)

echo Finished
exit /b 0
