from termcolor import colored  # module for colored text
import os
import time
import subprocess
import getpass
from sys import argv
import shutil
import distro
import threading
# ------------------------
from scripts import utilityy as utl
from scripts import fixerr
from scripts import multimedia as mm
from scripts import internet as intr
from scripts import devp as dv


subprocess.run(["clear"])
# --------------------------------------------------------------------------------------------------------------------------------


class logo():

    def logo1():

        print(colored(
            "-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-", "cyan", attrs=['bold']))
        print(colored("  _____         _____ _    _ _____ _______ ",
              "green", attrs=['bold']))
        print(colored(" / ____|  /\   / ____| |  | |_   _|__   __|",
              "cyan", attrs=['bold']))
        print(colored(
            "| (___   /  \ | |    | |__| | | |    | |   ", "yellow", attrs=['bold']))
        print(colored(" \___ \ / /\ \| |    |  __  | | |    | |   ",
              "blue", attrs=['bold']))
        print(colored(" ____) / ____ \ |____| |  | |_| |_   | |   ",
              "magenta", attrs=['bold']))
        print(colored("|_____/_/    \_\_____|_|  |_|_____|  |_|          -Do good. Be Ethical.",
              "white", attrs=['bold']))
        print(colored(
            "-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-\n", "cyan", attrs=['bold']))

    def logo4():

        print(colored(
            "═════════════════════════════════════════════════════", "cyan", attrs=['bold']))
        print(colored("  _____         _____ _    _ _____ _______ ",
              "magenta", attrs=['bold']))
        print(colored(" / ____|  /\   / ____| |  | |_   _|__   __|",
              "green", attrs=['bold']))
        print(
            colored("| (___   /  \ | |    | |__| | | |    | |   ", "cyan", attrs=['bold']))
        print(colored(" \___ \ / /\ \| |    |  __  | | |    | |   ",
              "yellow", attrs=['bold']))
        print(colored(" ____) / ____ \ |____| |  | |_| |_   | |   ",
              "blue", attrs=['bold']))
        print(colored(
            "|_____/_/    \_\_____|_|  |_|_____|  |_|          -Do good. Be Ethical.", "red", attrs=['bold']))
        print(colored(
            "═════════════════════════════════════════════════════\n", "cyan", attrs=['bold']))

    # animators
    logo1()
    time.sleep(1)
    subprocess.run(["clear"])
    logo4()
    time.sleep(1)
    subprocess.run(["clear"])
    logo1()
    time.sleep(1)
    subprocess.run(["clear"])
    logo4()


def banr():
    print(colored("   ═════════════════════════════════════════════════════",
          "white", attrs=['bold']))
    print(colored("    ____        _____ _____  _____ _____",
          "magenta", attrs=['bold']))
    print(colored("   |  _ \  _ __|  ___|_ _\ \/ /_ _|_   _|",
          "green", attrs=['bold']))
    print(colored("   | | | || '__| |_   | | \  / | |  | |  ",
          "cyan", attrs=['bold']))
    print(colored("   | |_| || |  |  _|  | | /  \ | |  | |  ",
          "yellow", attrs=['bold']))
    print(colored("   |____(_)_|  |_|   |___/_/\_\___| |_| ",
          "blue", attrs=['bold']))
    print(colored("   ═════════════════════════════════════════════════════\n",
          "white", attrs=['bold']))


# =========================================================================================================================================================
drprompt = "DRFIXIT ~|"
continuePrompt = "\nPress Any Key to continue "
ain = "Already Installed :)"


class color:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
    LYELLOW = '\033[93m'
    XYZ = '\033[96m'
    LMAGENTA = '\033[95m'


def clearScr():
    os.system('clear')


def supdate():
    os.system('cd scripts && sudo ./update.sh')


class check_snap():
    def __init__(self):

        if not shutil.which('snap'):
            self.install()

    def install(self):
        print("installing required tool..to run this script...")
        time.sleep(3)
        print('checking distro...')
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == 'kali' or 'ubuntu' or 'parrotos':
            b = 'sudo apt install snapd && sudo systemctl enable --now snapd apparmor'
            os.system(f'{b}')

        elif dist == 'arch':
            os.system('git clone https://aur.archlinux.org/snapd.git')
            os.system('cd snapd')
            os.system('makepkg -si')
            os.system(
                'sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap')

        elif dist == 'fedora':
            os.system('sudo dnf install snapd')
            os.system('sudo ln -s /var/lib/snapd/snap /snap')

        elif dist == 'centos':
            os.system('sudo yum install epel-release')
            os.system(
                'sudo yum install snapd && sudo systemctl enable --now snapd.socket && sudo ln -s /var/lib/snapd/snap /snap')
            exit()
        elif dist == 'manjaro':
            os.system(
                'sudo pacman -S snapd && sudo systemctl enable --now snapd.socket')
            os.system('sudo ln -s /var/lib/snapd/snap /snap')

        elif dist == 'mint':
            os.system(
                'sudo rm /etc/apt/preferences.d/nosnap.pref && sudo apt update && sudo apt install snapd')

        else:
            try:
                os.system('sudo apt install snapd ')
            except os.error as errr:
                print("i was unable to install geany :( error=", errr)
                time.sleep(4)

                print('please submitt a issue in this link- https://github.com/SACHIT69/Dr.fixit/issues ||Any feedback would be greatly appreciated. Thank you')
                time.sleep(5)
                exit()


class upsnap():
    def __init__(self):
        print("Checking for Updates...")
        time.sleep(1)
        os.system("snap refresh")


class drfix:
    def __init__(self):
        clearScr()  # clear

        threading.Thread(target=check_snap).start()  # check snap in system
        threading.Thread(target=logo).start()  # to run parallely
        clearScr()  # clear screen
        banr()  # drfixit banner
        print(color.GREEN + '''
  〘-------------≪⊶≼ Programmed By SACHIT ≽⊷≫-------------〙
    ''' + color.CYAN + '''
                      ______
                     |ERRORS|
               
       〘1〙═〢 Errors while running [apt update] command
       〘2〙═〢 Update/ full upgrade linux
       〘3〙═〢 FIX no sound output
       〘4〙═〢 Bluetooth not working/ can't turn on
            ══════════════════════════
            |sᴏғᴛᴡᴀʀᴇs/ᴀᴘᴘ sᴛᴏʀᴇ ғᴏʀ ʟɪɴᴜx|
            ══════════════════════════ 
                    Version-2.2
            ════════════════════════════ 
           |ᴄᴀᴛᴀɢᴏʀɪᴇs ᴏғ sᴏᴛᴡᴀʀᴇs ᴛᴏ ɪɴsᴛᴀʟʟ|
            ════════════════════════════
            
       〘5〙═〢 Multimedia
       〘6〙═〢 Office
       〘7〙═〢 Internet
       〘8〙═〢 Developing/programming softwares
       〘9〙═〢 Utility Softwares/Extras
       〘0〙═〢 UPDATE SNAP and This Tool
       〘00〙═〢 CONTRIBUTORS/ABOUT ME
       〘99〙═〢 EXIT\n  

   〘-------------≪⊶≼ OTHER ≽⊷≫-------------〙
       〘11〙═〢 Internet SPEED TEST

     '''+color.LYELLOW+''' TYPE THE NAME OF SOFTWARES BELOW TO OPEN INSTALLED SOFTWARES
     
     ''')
        usrinput = input(color.GREEN+drprompt)
        clearScr()
        if usrinput == "5":
            Multimedia()
        elif usrinput == "6":
            office()
        elif usrinput == "7":
            internet()
        elif usrinput == "8":
            devlopments()
        elif usrinput == "9":
            utility()
        elif usrinput == "3":
            fixerr.nosound()
        elif usrinput == "4":
            fixerr.bt()

        elif usrinput == "2":
            fixerr.update()

        elif usrinput == "1":
            fixerr.uperror()

        elif usrinput == "0":
            upsnap()
            time.sleep(1)
            supdate()
        elif usrinput == "00":
            cont()

        elif usrinput == "11":
            intr.speedtest()    
        elif usrinput == "99":
            exit()
        elif usrinput == "\r" or usrinput == "\n" or usrinput == "" or usrinput == " ":
            self.__init__()
        else:
            try:
                print(os.system(usrinput))
            except:
                pass
        self.completed()

    def completed(self):
        input("Completed, press Enter key to go back")
        self.__init__()

# -----------------------


def cont():
    print(color.CYAN+'''Greets TO Dibash Thapa ''' +
          color.GREEN+'''
     
     
            About me
       Name-Sachit Yadav
          AGE- 17 yrs
          From- Nepal
    ''')


class Multimedia:
    banner = '''
     __  __       _ _   _                    _ _       
    |  \/  |_   _| | |_(_)_ __ ___   ___  __| (_) __ _ 
    | |\/| | | | | | __| | '_ ` _ \ / _ \/ _` | |/ _` |
    | |  | | |_| | | |_| | | | | | |  __/ (_| | | (_| |
    |_|  |_|\__,_|_|\__|_|_| |_| |_|\___|\__,_|_|\__,_|
    '''

    def __init__(self):
        clearScr()
        print(color.XYZ+self.banner)

        print("  〘1〙═〢VLC media player")
        print("  〘2〙═〢spotify")
        print("  〘3〙═〢Rythmbox (music player)")
        print("  〘4〙═〢GIMP- GNU image Manipulation program(photoshop alternative) ")
        print("  〘5〙═〢Audacity (Audio software for multi-track recording and editing)")
        print("  〘6〙═〢Shotcut Best video editor")
        print("  〘55〙═〢Back To Main Menu \n")
        usrinput2 = input(color.WHITE+drprompt)
        clearScr()
        if usrinput2 == "1":
            mm.vlc()
        elif usrinput2 == "2":
            mm.spotify()
        elif usrinput2 == "3":
            mm.Rythmbox()
        elif usrinput2 == "4":
            mm.GIMP()
        elif usrinput2 == "5":
            mm.adcity()
        elif usrinput2 == "6":
            mm.shotcut()

        elif usrinput2 == "55":
            drfix()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input(color.GREEN+"Completed, press Enter key to go back")
        self.__init__()
# ----------------------------------------------------------------


class snapupdate():
    def __init__(self):
        print("checking for Update in snap")
        time.sleep(1)

        os.system("sudo snap refresh")
        time.sleep(1)


'''
OFFICE Softwares
'''


class office:
    banner = '''
      ___  _____ _____ ___ ____ _____ 
    / _ \|  ___|  ___|_ _/ ___| ____ |
    | | | | |_  | |_   | | |   |  _|  
    | |_| |  _| |  _|  | | |___| |___ 
    \___/|_|   |_|   |___\____|______|

    '''

    def __init__(self):
        clearScr()
        print(color.GREEN+self.banner)

        print(" 〘1〙═〢 Libre office (alternative for MS office)")

        print(" 〘66〙═〢Back To Main Menu \n")

        usrinput3 = input(drprompt)
        clearScr()
        if usrinput3 == "1":
            libof()
        elif usrinput3 == "66":
            drfix()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input(color.GREEN+"Completed, press Enter key to return to main menu")
        self.__init__()


class libof():
    def __init__(self):
        print(color.GREEN+"Checking if libreoffice is installed or not.")
        if not shutil.which('libreoffice'):
            self.install()

        else:
            print(ain)

    def install(self):
        print(color.GREEN+"Installing libreoffice...")
        os.system("sudo snap install libreoffice")


# =----------------------------------------------------------------------
class internet():
    banner = '''
     ___ _   _ _____ _____ ____  _   _ _____ ______
    |_S_| \ | |_ A _| _C__|  H \| \H| | __I_|_ T  _|
     | ||  \| | | | |  _| | |_) |  \| |  _|   | |
     | || |\  | | | | |___|  _ <| |\  | |___  | |  
    |___|_| \_| |_| |_____|_| \_\_| \_|_____| |_|  
    '''

    def __init__(self):
        clearScr()
        print(color.LYELLOW+self.banner)

        print(" 〘1〙═〢Google Chrome")
        print(" 〘2〙═〢Mozilla Firefox")
        print(" 〘3〙═〢Chromium")
        print(" 〘4〙═〢Thundermail mailer ")
        print(" 〘5〙═〢Discord")
        print(" 〘6〙═〢Brave Browser")
        print(" 〘7〙═〢Opera browser")
        print(" 〘77〙═〢Back To Main Menu \n")

        usrinput4 = input(color.XYZ+drprompt)
        clearScr()
        if usrinput4 == "1":
            intr.gchrome()

        elif usrinput4 == "2":
            print('this is under devlopment')    
        elif usrinput4 == "4":
            intr.mozilla()
        elif usrinput4 == "3":
            intr.Chromium()
        elif usrinput4 == "4":
            intr.thmailer()
        elif usrinput4 == "5":
            intr.discord()
        elif usrinput4 == "6":
            intr.bravebrowser()
        elif usrinput4 == "7":
            intr.opera()
        elif usrinput4 == "77":
            drfix()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input(color.LYELLOW+"Completed,press Enter key to go back")
        self.__init__()


# -------------------------------------------------------------------------------------------------------------


# class development and programming

class devlopments:
    banner = '''
     ____                 _                                  _   
    |  _ \  _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
    | | | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
    | |_| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
    |____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                                 |_|                             
    '''

    def __init__(self):
        clearScr()
        print(color.WHITE+self.banner)

        print("  〘1〙═〢 Pycharm CE")
        print("  〘2〙═〢 VS code")
        print("  〘3〙═〢 Sublime text")
        print("  〘4〙═〢 Beekeeper Studio ")
        print("  〘5〙═〢 Android Studio")
        print("  〘6〙═〢 Php Storm")
        print("  〘7〙═〢 Flutter")
        print("  〘8〙═〢 Atom")
        print("  〘88〙═〢Back To Main Menu \n")

        usrinput5 = input(color.RED+drprompt)
        clearScr()
        if usrinput5 == "1":
            dv.pycharm()

        elif usrinput5 == "2":
            dv.vscode()

        elif usrinput5 == "3":
            dv.sublimetext()

        elif usrinput5 == "4":
            print('under development')

        elif usrinput5 == "5":
            dv.andstudio()

        elif usrinput5 == "6":
            print("under development")

        elif usrinput5 == "7":
            print("under development")
            

        elif usrinput5 == "8":
            dv.atom()

        elif usrinput5 == "88":
            drfix()

        else:
            self.__init__()
        self.completed()

    def completed(self):
        input(color.GREEN+"Completed,press Enter key to go back")
        self.__init__()


# class utility Softwares

class utility:
    banner = '''
     _   _ _____ ___ _     ___ _______   __
    | | | |_   _|_ _| |   |_ _|_   _\ \ / /
    | | | | | |  | || |    | |  | |  \ V / 
    | |_| | | |  | || |___ | |  | |   | |  
     \___/  |_| |___|_____|___| |_|   |_|  
                                       

    '''

    def __init__(self):
        clearScr()
        print(color.GREEN+self.banner)

        print("  〘1〙═〢 Stacer(best GUI system monitor software")
        print("  〘2〙═〢 Geany GUI text editor")
        print("  〘3〙═〢 OBS video recorder")
        print("  〘4〙═〢 Ksnip Screeshot tool ")
        print("  〘5〙═〢 Microsoft Teams")
        print("  〘6〙═〢 qbittorrent")
        print("  〘7〙═〢 Uget Download Manager")
        print("  〘8〙═〢 Geforce Now for NDVIDIA GPU ||Drivers ")
        print("  〘9〙═〢 Kdenlive Best Video editor")
        print("  〘0〙═〢 Handbrake")
        print("  〘99〙═〢Back To Main Menu \n")

        usrinput6 = input(drprompt)
        clearScr()
        if usrinput6 == "1":
            utl.stacer()

        elif usrinput6 == "2":
            utl.geany()

        elif usrinput6 == "3":
            utl.obs()

        elif usrinput6 == "4":
            utl.ksnip()

        elif usrinput6 == "5":
            utl.msteam()
        elif usrinput6 == "6":
            utl.qbit()

        elif usrinput6 == "7":
            utl.uget()
        elif usrinput6 == "8":
            utl.Gforce()
        elif usrinput6 == "9":
            utl.kedenlive()
        elif usrinput6 == "0":
            utl.handbrake()                

        elif usrinput6 == "99":
            drfix()

        else:
            self.__init__()
        self.completed()

    def completed(self):
        input(color.GREEN+"Completed,press Enter key to go back")
        self.__init__()


if __name__ == "__main__":

    try:
        drfix()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.45)
