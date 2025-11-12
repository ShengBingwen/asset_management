@echo off
REM -------------------------------
REM 启动资产管理系统（Flask + Vue）
REM -------------------------------

REM 1. 启动 Flask 后端
start "Flask Server" cmd /k "cd /d D:\VS Code\Projects\asset_management\backend && ..\.venv\Scripts\activate.bat && python server.py"

REM 2. 启动 Vue 前端
start "Vue Frontend" cmd /k "cd /d D:\VS Code\Projects\asset_management\frontend && npm run dev"

REM 3. 打开浏览器访问 Vue 前端
timeout /t 5 >nul
start http://localhost:5173

echo.
echo ======================================
echo 系统启动完成，请在打开的窗口查看后端和前端日志。
echo ======================================
pause