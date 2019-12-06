@echo off
echo.
echo ____________________________________________________________
echo ##                  Python Project Setup                  ##
echo ____________________________________________________________
echo.

SET BUILD_DIR=%CD%
ECHO You are in %BUILD_DIR%
ECHO.


PUSHD ..
SET PROJECT_DIR=%CD%
SET BIN_DIR=%PROJECT_DIR%\bin
IF NOT EXIST bin MKDIR bin
ECHO ** The binaries directory is set to %BIN_DIR%
ECHO ** The project directory is set to %PROJECT_DIR%
ECHO.
POPD

WHERE python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO *! Python wasn't found. 
    ECHO *! Install Python 3 or add it to your PATH.
    ECHO *! Project setup will close.
    GOTO END_SETUP
) ELSE (
    ECHO ** Python found. Proceeding...
)


REM Creating virtual environment
ECHO.
ECHO ** Creating virtual environment ... 

PUSHD ..
CD %BIN_DIR%
IF NOT EXIST diet_env (
    MKDIR diet_env
)
SET ENV=%CD%\diet_env
ECHO ** ...in %ENV%
POPD 

python -m venv %ENV% --clear --prompt DIET 
IF %ERRORLEVEL% NEQ 0 (
    ECHO **!
    ECHO **! Error in python command
    ECHO **! Check that you have Python 3.7 installed
    ECHO **! Install it in your local programs folder and pass it as an argument
    GOTO END_SETUP
)
ECHO ** [OK] Virtual environment created
ECHO ** Activating...

PUSHD %ENV%\Scripts
CMD /K "activate.bat && python -m pip install --upgrade pip && cd %BUILD_DIR% && pip.exe install -r requirements.txt"

:END_SETUP
EXIT /b 0
