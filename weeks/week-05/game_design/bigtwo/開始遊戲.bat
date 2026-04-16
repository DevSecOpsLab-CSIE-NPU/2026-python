@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo       大老二 Big Two 遊戲
echo ========================================
echo.
pip install pygame -q
python main.py
pause
