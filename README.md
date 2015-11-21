# Smoker Beacon

Take the output from a thermocouple, input through an SBC and transmit via Wi-Fi to a collector. 
Send temperature telemetry for a smoker.

# App

Receives output showing the temperature from one or more thermocouples  
Configurable mix/max temperature alarm  
(not included in this repo)

Items needed:
* pcDuino3 http://www.linksprite.com/?page_id=812
* csr bluetooth V4 dongle

TL;DR - To run the system by hand, execute dispatcher and thermocouple scripts.
```
cd smoker-beacon
source venv/bin/activate
python dispatcher.py
python sb.py
```
##Field Guide
* Hook up a USB keyboard, preferably with built-in mouse
* Use a USB hub to connect more than one device
* Hit CTRL-ALT-T to open a Terminal
* Hit ALT-TAB to switch between Terminal and Application
* Logs are located in /var/log/smoker-beacon
* Startup log located in /home/linaro/logs/cronlog
* Key programs are "sb.py" and "dispatcher.py"
* Programs are located in /home/linaro/smoker-beacon
* The order: attach thermocouple first, then turn on CPU unit
* Calibrate the thermocouple when setting up, 

##TODO

##Objective: Thermocouple readings through beacon to app

System Installation Requirements
* ZeroMQ
* Python
* iPython
* supervisor

Python Installation Requirements
* pillow
* pyserial
* python-serial
* transitions
* virtualenv development environment


## Platform preparation
1. Generate a key using 'ssh-keygen -t rsa' (take the defaults on prompts)
1. [Upload a Deploy Key](https://github.com/dixon1e/smoker-beacon/settings/keys) and clone [this repo](https://github.com/dixon1e/smoker-beacon) using the id_rsa.pub key

        git clone git@github.com:dixon1e/smoker-beacon.git

1. Install all Ubuntu Linux packages (build-essential already included)

        sudo apt-get update && sudo apt-get upgrade -y
        sudo apt-get install -y python-pip python-virtualenv python-dev curl 
        sudo apt-get install -y python-bluez

1. Set the correct Time Zone

        sudo timedatectl set-timezone America/Denver

1. Install the supervisor package

        sudo pip install supervisor

5. Create a virtualenv in the repo directory (/home/linaro/smoker-beacon)
 
        cd ~/smoker-beacon
        virtualenv venv --no-site-packages

1. Activate virtual environment

        . ./venv/bin/activate
        
1. Install the Python libraries

        pip install -r requirements.txt
        
1. Test run scripts for thermocouple reader (sb.py):

        cd ~/smoker-beacon
        . ./venv/bin/activate (if you have not already done this)
        python sb.py
        python dispatcher.py

1. Add a new job to crontab for root user

        sudo su -  
        crontab -e 
        
        (make the following the last line)  
        
        @reboot su linaro -c "DISPLAY=:0.0 sh /home/linaro/smoker-beacon/startall.sh >/home/linaro/logs/cronlog 2>&1"

1. Change Desktop Background

        Open "Preferences >" | "Desktop Preferences" panel (from from lower left icon in Desktop Toolbar)
        In the "Appearance" Tab, change the "Wallpaper", opens new panel
                Browse to: "Filesystem" | "/smoker-beacon/images/logo.png"
                Click "Open"
				Click Background Color and change to "White", e.g. 255, 255, 255 in the R,G,B fields
        Click "Close"

1. Check dispatcher.py and sb.py to make sure Logging level is not more than "WARNING"

## State Machine Description

## Bluetooth (future) 
