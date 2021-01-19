@echo off
color 4
title pinger
echo.
:hub
cls
set /p var=IP: 
title pinging ~%var%~
:d
:x
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
PING -l 1 -n 1 %var% | FIND "TTL="
IF ERRORLEVEL 1 goto f
GoTo d
:f
echo offline
color 04
goto x
