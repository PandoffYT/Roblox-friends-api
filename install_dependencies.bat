@echo off
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "pyver=Your current version of python is %%i"
title %pyver%
echo This script installs the required python "extensions" for the script to work, make sure you have python installed
echo If the title bar says something like "Your current version of python is Python 3.13.2", you're good to go
echo If not, go on python's official website, download python and make sure to check the button where it says add python to path
echo After that, run this script again
pause
pip install winshell
pip install pywin32
pip install requests
echo Done! Check the output to see if anything went wrong, you can now press any key/close this window
pause
exit