import time
import os
import shutil
from scripts import multimedia as mm
ain = "Already Installed"


# sub class for INTERNET

class gchrome():
    def __init__(self):
        print(mm.color.GREEN+"Checking if google chrome is installed or not...")
        if not shutil.which('google-chrome'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("downloading chrome...")
        os.system(
            "curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o a.deb ")
        print("Downloaded ! installing it")
        os.system("sudo dpkg -i a.deb")
        os.system("sudo rm -rf a.deb")
        print("All done !!")


class mozilla():
    def __init__(self):
        print(mm.color.GREEN+"Checking if firefox is installed or not...")
        if not shutil.which('firefox'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("working on this...wait for update")


class bravebrowser():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Bravebrowser is installed or not...")
        if not shutil.which('brave'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("brave is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("snap install brave")
        print("Brave browser installed !")


class Chromium():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Chromium is installed or not...")
        if not shutil.which('chromium'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("Chromium is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("snap install chromium")
        print("Chromium browser installed !")


class thmailer():
    def __init__(self):
        print(mm.color.GREEN+"Checking if thundebird mailer is installed or not...")
        if not shutil.which('thunderbird'):
            self.install()

        else:
            print(ain)

    def install(self):
        print(" is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("snap install thunderbird ")
        print("Thunderbird mailer installed !")


class opera():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Opera is installed or not...")
        if not shutil.which('opera'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("Opera is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("snap install opera")
        print(" installed !")


class discord():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Discord is installed or not...")
        if not shutil.which('discord'):
            self.install()

        else:
            print(ain)

    def install(self):
        print("Discord is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("snap install discord")
        print(" installed !")


class speedtest():
    
    def __init__(self):
        
        if not shutil.which('speedtest-cli'):
            self.spdrun()

        else:
            self.run()

    def run(self):
        os.system('speedtest-cli')
        
            
            
    def spdrun(self):
        os.system('python3 -m pip install speedtest-cli')
        time.sleep(2)
        os.system('export PATH="$PATH:$HOME/.local/bin"')
        os.system('clear')
        os.system('speedtest-cli')





