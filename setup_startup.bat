@echo off
echo Setting up Outplayed Auto-Uploader to run on PC startup...

:: Get the current directory
set SCRIPT_DIR=%~dp0
set MAIN_FILE=%SCRIPT_DIR%main.py

:: Path to the Windows Startup folder
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_NAME=OutplayedUploader.bat

:: Create a small batch file in the startup folder that runs the python script
echo @echo off > "%STARTUP_FOLDER%\%SHORTCUT_NAME%"
echo cd /d "%SCRIPT_DIR%" >> "%STARTUP_FOLDER%\%SHORTCUT_NAME%"
echo python main.py >> "%STARTUP_FOLDER%\%SHORTCUT_NAME%"

echo.
echo Success! The script will now run automatically when you turn on your PC.
pause
