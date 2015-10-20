REM Use the DOS prompt as a rudimentary D'ni clock
REM Exit with ctrl-c
@echo off
mode con: cols=35 lines=3
setlocal enableextensions enabledelayedexpansion
set /a "x = 0"
:while1
	echo.
	python dnitime.py
	timeout 1 > NUL
	goto :while1
endlocal
