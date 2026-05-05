@echo off

echo.
echo LeadScript - arraste um arquivo .las em dist\leadscript.exe
echo ou informe o caminho como primeiro argumento deste .bat.
echo.

if "%~1"=="" (
    echo Uso: executar.bat caminho\para\script.las
) else (
    dist\leadscript.exe rodar "%~1" --pausar
)

pause
