GettingStartedUsingWindowsExe - Quick guide to using Pigeon Feather exe

# Introduction #

This is a short guide explaining the steps needed to use Pigeon Feather using the Windows Exe.  This exe file is produced using py2exe and should be stable enough for real world usage although it has very little testing by myself the project creator.

# Requirements for Pigeon Feather using the Windows/py2exe build #

MSVCR90.dll is required for the exe to work.  You may already have this installed.  The best way to proceed is to download and run the Pigeon Feather exe.  If you encounter the error:

`This application has failed to start because the application configuration is incorrect.  Reinstalling the application may fix this problem`

Then you should download and install the freely available vcredist\_x86.exe which can be obtained from  http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en  This package contains the required MSVCR90.dll

# Invocation #

Download the py2exe build from http://code.google.com/p/pigeonfeather/downloads/list, unzip the archive and start Pigeon Feather by double clicking the file pigeonfeather.exe

# Configuration #

A Woeid is required to retrieve the weather for your location.  Information on how to obtain a Woeid for your location can be found here ObtainingWoeid