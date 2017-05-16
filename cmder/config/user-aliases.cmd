::shell=
ls=ls --show-control-chars -F --color $*
pwd=cd
clear=cls
history=cat %CMDER_ROOT%\config\.history
grep=grep --color $*
grepx=grep --color -nriC $*
find=find . -name $*
unalias=alias /d $*


::tools=
e.=explorer .
subl="sublime_text.exe" $*


::python=
py="python" $*
ipy=ipython
jpy=cmd /k "jupyter qtconsole --style=monokai" -new_console:t:"Jupyter" -new_console:b
jpyn=jupyter notebook -new_console:t:"Jupyter Notebook" -new_console:b
spy=spyder -new_console:t:"Spyder" -new_console:b

::git=
g= git $*
gf=git flow $*

::add,commit,push=
ga= git add
gaa= git add .
gan= git add -n .
gaundo= git reset HEAD
gac=git commit -am $*
gc= git commit -m $*
gcundo=git commit --amend
gp=git push $*
gpo=git push origin $*

::status=
gs=git status --short --branch $*
gl=git log --oneline --all --graph --decorate $*
gls=git ls-files $*
gd= git diff --color-words $*

::branch=
gch=git checkout $*
gb=git branch $*
gm=git merge $*
gt=git tag $*
grst-h=git reset --hard  HEAD  
