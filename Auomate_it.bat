@Echo Off
setlocal
ping 127.0.0.1 -n 2 > nul
Echo Neobux-PTC Automation [Version 1.2.10506.345]
Echo (c) 2019 Automate Corporation. All right reserved.
Echo.
ping 127.0.0.1 -n 2 > nul
::Display Content
Echo ===================================================
Echo Enviroment Setup ---- Part 2
Echo ===================================================
ping 127.0.0.1 -n 2 > nul
Echo.
Echo 	     Configuring Automation....
ping 127.0.0.1 -n 4 > nul
::Any error
Echo Error List:
python -c "import sys; print(sys.executable)" > tem.txt
SET /p exe=< tem.txt
Echo.
Echo ---------------------------------------------------
::Check For Error
IF "%exe%" EQU "" (GOTO END) 

::Details for use
ping 127.0.0.1 -n 2 > nul
Echo Fetch Details.....
:: 1st parameter
ping 127.0.0.1 -n 4 > nul
Echo.
Echo Program/Script info :
Echo   = %exe%  
:: 2nd parameter
Echo.
Echo Add argument info :
Echo   = Main.py
:: 3rd parameter
Echo.
Echo Start in info :
Echo   = %cd%
Echo.
ping 127.0.0.1 -n 2 > nul
Echo ---------------------------------------------------
:: Setup Task Sheduler
timeout /t 2
Echo.
Echo *** Reffer the Tsetup.PDF given with the program and setup the TaskSheduler. ***
Echo Enter to proceed with TaskSheduler...
pause > nul
taskschd.msc
GOTO OVER
:END
Echo. TroubleShooting.....
ping 127.0.0.1 -n 5 > nul
Echo Enviorement requirement ERROR
Echo Hints to fix error-
Echo   --Install Python
Echo   --Add Pthon to your PATH VARIABLE
::ping 127.0.0.1 -n 2 > nul
Echo.
Echo Fullfill the requirement and Try Again !!
Echo Enter to continue...
pause > nul
:OVER
endlocal