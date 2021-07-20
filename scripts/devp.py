import os
import shutil
import time
import scripts.functions as er
from scripts import multimedia as mm

ain = "Already Installed"


class pycharm:
    def __init__(self):
        print(mm.color.GREEN + "Checking if Pycharm is installed or not...")
        if not shutil.which(""):
            self.install()

        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.GREEN + "Pycharm CE is not installed !!")
        time.sleep(1.5)
        print(mm.color.GREEN + "Installing...")
        os.system("sudo snap install pycharm-community --classic")
        print(mm.color.GREEN + " Pycharm CE installed !")


class vscode:
    def __init__(self):
        print(mm.color.GREEN + "Checking if visual studio code is installed or not...")
        if not shutil.which("code"):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Vs code is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        os.system("sudo snap install code --classic")
        time.sleep(1)
        print(mm.color.LYELLOW + "Visual studio code installed !!")


class sublimetext:
    def __init__(self):
        print(mm.color.GREEN + "Checking if Sublime text is installed or not...")
        if not shutil.which(""):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Sublime text is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        os.system("sudo snap refresh && sudo snap install sublime-text --classic")
        print(mm.color.LYELLOW + "Sublime text installed !!")


class atom:
    def __init__(self):
        print(mm.color.GREEN + "Checking if Atom is installed or not...")
        if not shutil.which("atom"):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Atom is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        try:
            os.system("sudo snap refresh && sudo snap install atom --classic")
        except os.error:
            print(mm.color.LYELLOW + "i was unable to install atom")
            time.sleep(2)
            er.issue("Atom")


class andstudio:
    def __init__(self):
        print(mm.color.GREEN + "Checking if Android Studio is installed or not...")
        if not shutil.which("android-studio"):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Android studio is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        try:
            os.system(
                "sudo snap refresh && sudo snap install android-studio --classic")
        except os.error:
            print(mm.color.LYELLOW + "i was unable to install Android studio")
            time.sleep(2)
            er.issue("Android Studio")


class flutterInst:
    def __init__(self):
        print(mm.color.GREEN + "Checking if Flutter is installed or not...")
        if not shutil.which("flutter"):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Flutter is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        try:
            os.system("sudo snap refresh && sudo snap install flutter --classic")
        except os.error:
            print(mm.color.LYELLOW + "i was unable to install flutter")
            time.sleep(2)
            er.issue("Flutter")


class phpStormInst:
    def __init__(self):
        print(mm.color.GREEN + "Checking if PHP Storm  is installed or not...")
        if not shutil.which("phpstorm"):
            self.install()
        else:
            print(mm.color.GREEN + ain)

    def install(self):
        print(mm.color.LYELLOW + "Php Storm  is not installed !!")
        time.sleep(1.5)
        print(mm.color.LYELLOW + "Installing...")
        try:
            os.system("sudo snap refresh && sudo snap install phpstorm --classic")
        except os.error:
            print(mm.color.LYELLOW + "i was unable to install phpstorm")
            time.sleep(2)
            er.issue("Php Storm")
