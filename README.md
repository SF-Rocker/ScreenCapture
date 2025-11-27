# Uses Grim + Scrot for wayland compistor environment, and uses maim -s for x11 environemnt uses screenshot click and drag selection.
Screenshot Tool for Terminal on XFCE and KDE setups mainly for my singleboard computers without a Print Screen Function
Set it up for a shortcut

rename filename.py to anyname.py

`touch filename.py`

`sudo -s`

```nano filename.py```                     

CTRL + O, CTRL + X


* Control + O to save; Control + X to Exit.

 # copy and paste code into terminal with CTRL + C, and in terminal use CTRL + SHIFT + V to paste code into nano code editer; you can use vi for vim, it is your preference.
```python3 filename.py
            or
            
            python3 anyname.py 

            Go To Settings Keyboard, and use a bash script to put the filename in order.
            sudo -s 
            
            touch filename.sh 
            
            nano filename.sh 

            paste: #!/bin/bash
            python3 /home/tj/screen.py

            CTRL + X to save and exit.

            Run ./filename.sh in terminal first to install pre-requisites or dependencies.

            In Keyboard Shortcuts from Settings click + button add and type ./filename.sh
            
            and press the Prt Scr Sys Rq button and now click yes use ./filename.py instead.
            and you should have everything working now.

            
