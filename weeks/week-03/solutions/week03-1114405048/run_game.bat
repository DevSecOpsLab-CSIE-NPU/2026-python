@echo off
setlocal
cd /d %~dp0

echo [Robot Lost] Launching game...
d:\1114405048\.venv\Scripts\python.exe robot_game.py

echo.
echo [Robot Lost] Process finished with exit code %ERRORLEVEL%.
pause

endlocal
