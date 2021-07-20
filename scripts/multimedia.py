import os
import shutil
import time
import scripts.functions as er
ain = "Already Installed"


class color:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[36m"
    WHITE = "\033[97m"
    LYELLOW = "\033[93m"
    XYZ = "\033[96m"
    LMAGENTA = "\033[95m"


# ----------------------------------------------------------------
class vlc:
    def __init__(self):
        print(color.GREEN + "Checking vlc is installed or not...")
        if not shutil.which("vlc"):
            print(color.GREEN + "Found not installed")
            time.sleep(1)
            print(color.GREEN + "Installing...")
            self.install()

        else:
            print(color.GREEN + ain)

    def install(self):
        try:
            os.system("snap install vlc")
        except OSError:
            er.issue("Vlc")
            exit()


# ----------------------------------------------------------------
class spotify:
    def __init__(self):
        print(color.GREEN + "CHecking if spotify is installed or not..")
        if not shutil.which("spotify"):
            time.sleep(1.5)
            print(color.GREEN + "Not installed, installing it...")
            self.install()
            print(color.GREEN + "spotify installed")

        else:
            print(color.GREEN + ain)

    def install(self):
        try:
            os.system("snap install spotify")
        except OSError:
            er.issue("Spotify")
            exit()


# ----------------------------------------------------------------
class Rythmbox:
    def __init__(self):
        print(color.GREEN + "checking if Rythmbox is installed or not.")
        if not shutil.which("rhythmbox"):
            sleep(1.5)
            print(color.GREEN + "Not installed, installing it...")
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("apt install rhythmbox")
        except OSError:
            er.issue("Rhythmbox")
            exit()


# ----------------------------------------------------------------
class GIMP:
    def __init__(self):
        print(color.GREEN + "Checking if GIMP is installed or not.")
        if not shutil.which("gimp"):
            time.sleep(1.5)
            print(color.GREEN + "Not installed, installing it...")
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("snap install gimp")
        except OSError:
            er.issue("GIMP")
            exit()


class adcity:
    def __init__(self):
        print(color.GREEN + "Checking if audacity is installed or not.")
        if not shutil.which("audacity"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("snap install audacity")
        except OSError:
            er.issue("Audacity")
            exit()


class shotcut:
    def __init__(self):
        print(color.GREEN + "Checking shotcut in system...")
        if not shutil.which("shotcut"):
            self.install()
        else:
            print(ain)

    def install(Self):
        try:
            os.system("snap install shotcut --classic")
        except os.error:
            er.issue("Shotcut")
