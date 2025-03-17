@echo off
:: Check if running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting Administrator privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c ""%~f0""' -Verb RunAs" 
    exit /b
)

:: Detect Windows Version
for /f "tokens=4-5 delims=. " %%a in ('ver') do (
    if "%%a.%%b"=="6.1" (
        echo Windows 7 detected.
        echo Installing python-3.8.5.exe...
        "%~dp0windows7\setup\python-3.8.5.exe" /passive InstallAllUsers=1 PrependPath=1 Include_test=0
        
        echo Installation complete.

        :: Ensure pip.py exists before execution
        if exist "%~dp0pip-w7.py" (
            python "%~dp0pip-w7.py"
        ) else (
            echo Warning: pip-w7.py not found. Skipping execution.
        )
    )
    if "%%a"=="10" (
        echo Windows 10 detected.
        
        echo Installing python-3.11.0-amd64.exe...
        "%~dp0windows10\setup\python-3.11.0-amd64.exe" /passive InstallAllUsers=1 PrependPath=1 Include_test=0

        echo Installation complete.

        :: Ensure pip.py exists before execution
        if exist "%~dp0pip-w10.py" (
            python "%~dp0pip-w10.py"
        ) else (
            echo Warning: pip-w10.py not found. Skipping execution.
        )
    )
)

python "%~dp0start.py"