import subprocess
import os

import time


class color:
    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
    LYELLOW = '\033[93m'
    XYZ = '\033[96m'
    LMAGENTA = '\033[95m'

def clr():
    os.system('clear')

def nosound():
    clr()
    time.sleep(2)
    print(color.GREEN+"Installing pulse audio_audio manager")
    time.sleep(2)
    os.system('sudo apt install pulseaudio')
    print(color.CYAN+"Turning on pulse audio and its services")
    time.sleep(2)
    os.system('sudo systemctl --user enable pulseaudio && systemctl --user start pulseaudio')
    time.sleep(2)
    clr()
    time.sleep(1)
    print(color.GREEN+"Check if sound is available in output !!")
    time.sleep(4.5)
    print(color.GREEN+"that was at least i could do :)")
    time.sleep(4)
    print(color.GREEN+"IF, it wasn't fix, try rebooting your system..")
    time.sleep(4)  

def bt():
    clr()
    time.sleep(2)
    print(color.GREEN+"searching For issue in Bluetooth")
    time.sleep(2)
    print(color.GREEN+"Restarting Bluetooth manager services")
    time.sleep(3)
    os.system('sudo service bluetooth restart ')
    time.sleep(3)
    print(color.GREEN+"Check if bluetooth is enabled or not..")
    time.sleep(3)


def uperror():
    clr()
    print(color.CYAN+"error while updating packages?,and while installing packages?")
    time.sleep(2)
    print(color.GREEN+"wait, i will fix this..")
    print(color.GREEN+"working on issue...")
    time.sleep(3)
    print(color.GREEN+"wait a while, this may take more time !")
    time.sleep(1.5)
    os.system('sudo apt update --fix-missing && sudo apt --fix-broken install')      
    time.sleep(2)
    print(color.CYAN+"Everything done.. !!")

def update():
    clr()
    print(color.GREEN+"updating...")   
    time.sleep(3)
    print(color.GREEN+"This may take more time, wait..")
    time.sleep(1.5)
    os.system('sudo apt update -y && sudo apt full-upgrade -y')
    time.sleep(2.5)
    print(color.GREEN+"DONE !!")
    time.sleep(2.5)