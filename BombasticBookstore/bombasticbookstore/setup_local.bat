@echo off
echo Setting up Bombastic Bookstore locally...

:: Ensure Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b
)

echo Creating a virtual environment...
python -m venv venv
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to create virtual environment.
    pause
    exit /b
)

echo Activating virtual environment...
call venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b
)

echo Upgrading pip...
pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to upgrade pip.
    pause
    exit /b
)

echo Installing required packages...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install packages.
    pause
    exit /b
)

echo Starting the server...
start python manage.py runserver

echo Setup complete! You can now access the application in your browser.
pause
