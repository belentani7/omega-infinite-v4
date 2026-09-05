# Start script for Omega Infinite OS
Write-Host "Instalando dependencias de Python..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host "Iniciando backend OMEGA CORE (FastAPI)..." -ForegroundColor Red
Start-Process "uvicorn" -ArgumentList "backend:app --host 0.0.0.0 --port 8000" -NoNewWindow

Write-Host "Backend en ejecución. Abre index.html en tu navegador." -ForegroundColor Green
Start-Process "index.html"
