@echo off
python --version >nul 2>&1
if %errorlevel%==0 (

    echo Python installed.
    for /f "tokens=4-5 delims=. " %%a in ('ver') do (
        if "%%a.%%b"=="6.1" (
            echo Windows 7 detected.
            echo Installing or Upgrading required pip library...
            pip install openpyxl
            pip install PyPDF2
            pip install python-docx
            start "" "start.py"
            exit
        )
        if "%%a"=="10" (
            echo Windows 10 detected.
            echo Installing or Upgrading required pip library...
            pip install openpyxl
            pip install PyPDF2
            pip install python-docx
            pip install pillow
            start "" "start.py"
            exit
        )
        else (
            echo Unsupported Windows version.
            pause
            exit
        )
    )
    exit
) else (
    for /f "tokens=4-5 delims=. " %%a in ('ver') do (
        if "%%a.%%b"=="6.1" (
            echo Windows 7 detected.
            echo Installing Python...
            start /wait "" "%~dp0windows7\setup\python-3.8.5.exe"
            echo Installing or Upgrading required pip library...
            pip install openpyxl
            pip install PyPDF2
            pip install python-docx
            start "" "start.py"
            exit
        )
        if "%%a"=="10" (
            echo Windows 10 detected.
            echo Installing Python...
            start /wait "" "%~dp0windows10\setup\python-3.11.0-amd64.exe"
            echo Installing or Upgrading required pip library...
            pip install openpyxl
            pip install PyPDF2
            pip install python-docx
            pip install pillow
            start "" "start.py"
            exit
        )
        else (
            echo Unsupported Windows version.
            pause
            exit
        )
    )
    exit
)
echo Unsupported Windows version.
pause
exit