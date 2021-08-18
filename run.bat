@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
REM
CALL D:\Anaconda3\Scripts\activate.bat D:\Anaconda3
python web.py