import shutil
import time
import os
ain = "Already Installed"

class color:
    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
    LYELLOW = '\033[93m'
    XYZ = '\033[96m'
    LMAGENTA = '\033[95m'
















#----------------------------------------------------------------
class vlc:
    def __init__(self):
        print(color.GREEN+"Checking vlc is installed or not...")
        if not shutil.which('vlc'):
            print(color.GREEN+"Found not installed")
            time.sleep(1)
            print(color.GREEN+"Installing...")
            self.install()
            
        else:
            print(color.GREEN+ain)
 
    def install(self):
        os.system("sudo snap install vlc")
#----------------------------------------------------------------
class spotify:
    def __init__(self):
        print(color.GREEN+"CHecking if spotify is installed or not..")
        if not shutil.which('spotify'):
            time.sleep(1.5)
            print(color.GREEN+"Not installed, installing it...")
            self.install()
            print(color.GREEN+"spotify installed")
            
        else:
            print(color.GREEN+ain)
    def install(self):
        os.system("sudo snap install spotify")    



#----------------------------------------------------------------
class Rythmbox:
    def __init__(self):
        print(color.GREEN+"checking if Rythmbox is installed or not.")
        if not shutil.which('rhythmbox'):
            sleep(1.5)
            print(color.GREEN+"Not installed, installing it...")
            self.install()            
        else:
            print(ain)
    def install(self):
        os.system("sudo apt install rhythmbox")                       
#----------------------------------------------------------------
class GIMP():
    def __init__(self):
        print(color.GREEN+"Checking if GIMP is installed or not.")
        if not shutil.which('gimp'):
            time.sleep(1.5)
            print(color.GREEN+"Not installed, installing it...")
            self.install()
        else:
            print(ain)
    def install(self):
        os.system("sudo snap install gimp")   


class adcity():
    def __init__(self):
        print(color.GREEN+"Checking if audacity is installed or not.")
        if not shutil.which('audacity'):
            self.install()
        else:
            print(ain)
            response = input(continuePrompt)
    def install(self):
        print("Installing audacity")
        os.system("sudo snap install audacity")
     
