import time
import os
import shutil
from scripts import multimedia as mm
ain = "Already Installed"


class pycharm():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Pycharm is installed or not...")
        if not shutil.which(''):
            self.install()

        else:
            print(mm.color.GREEN+ain)

    def install(self):
        print(mm.color.GREEN+"Pycharm CE is not installed !!")
        time.sleep(1.5)
        print(mm.color.GREEN+"Installing...")
        os.system("sudo snap install pycharm-community --classic")
        print(mm.color.GREEN+" Pycharm CE installed !")


class vscode():
    def __init__(self):
        print(mm.color.GREEN+"Checking if visual studio code is installed or not...")
        if not shutil.which('code'):
            self.install()
        else:
            print(mm.color.GREEN+ain)

    def install(self):
        print(mm.color.LYELLOW+"Vs code is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW+"Installing...")
        os.system("sudo apt install curl && curl https://az764295.vo.msecnd.net/stable/054a9295330880ed74ceaedda236253b4f39a335/code_1.56.2-1620838498_amd64.deb -o vs.deb")
        time.sleep(1)
        os.system("sudo dpkg -i vs.deb")
        time.sleep(1)
        os.system("sudo rm -rf vs.deb")
        print(mm.color.LYELLOW+"Visual studio code installed !!")


class sublimetext():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Sublime text is installed or not...")
        if not shutil.which(''):
            self.install()
        else:
            print(mm.color.GREEN+ain)

    def install(self):
        print(mm.color.LYELLOW+"Sublime text is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW+"Installing...")
        os.system("sudo snap refresh && sudo snap install sublime-text --classic")
        print(mm.color.LYELLOW+"Sublime text installed !!")




class atom():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Atom is installed or not...")
        if not shutil.which('atom'):
            self.install()
        else:
            print(mm.color.GREEN+ain)

    def install(self):
        print(mm.color.LYELLOW+"Atom is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW+"Installing...")
        try:
            os.system("sudo snap refresh && sudo snap install atom --classic")
        except os.error:
            print(mm.color.LYELLOW+"i was unable to install atom")
            time.sleep(2)
            print(mm.color.LYELLOW+"\nplease submitt issue in this link- https://github.com/SACHIT69/Dr.fixit/issues ||Any feedback would be greatly appreciated. Thank you")
                

class andstudio():
    def __init__(self):
        print(mm.color.GREEN+"Checking if Android Studio is installed or not...")
        if not shutil.which('android-studio'):
            self.install()
        else:
            print(mm.color.GREEN+ain)

    def install(self):
        print(mm.color.LYELLOW+"Android studio is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW+"Installing...")
        try:
            os.system("sudo snap refresh && sudo snap install android-studio --classic")
        except os.error:
            print(mm.color.LYELLOW+"i was unable to install Android studio")
            time.sleep(2)
            print(mm.color.LYELLOW+"\nplease submitt issue in this link- https://github.com/SACHIT69/Dr.fixit/issues ||Any feedback would be greatly appreciated. Thank you")
                
