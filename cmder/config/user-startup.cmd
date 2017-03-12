:: use this file to run your own startup commands 
:: use @ in front of the command to prevent printing the command

:: @call "C:\Program Files\Cmder\vendor\git-for-windows/cmd/start-ssh-agent.cmd
:: @set PATH=%CMDER_ROOT%\vendor\whatever;%PATH%

@prompt $E[1;32;40m$P$S{git}{hg}$S$_$E[1;30;40m$$$S$E[0m
::λを$マークに変更

@chcp 65001

cls
