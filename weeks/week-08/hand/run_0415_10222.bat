@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "0415#10222"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python "0415#10222"
    ) else (
        echo [ERROR] Python not found. Install Python or py launcher first.
    )
)

echo.
echo Press any key to exit...
pause >nul
