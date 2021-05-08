from termcolor import colored #module for colored text
import os 
import time
import subprocess
import getpass
from sys import argv
import shutil
import fixerr


subprocess.run(["clear"])
#--------------------------------------------------------------------------------------------------------------------------------
class logo():

    def logo1():
        
        print(colored("-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-", "cyan", attrs=['bold']))
        print(colored("  _____         _____ _    _ _____ _______ ", "green" , attrs=['bold']))
        print(colored(" / ____|  /\   / ____| |  | |_   _|__   __|", "cyan", attrs=['bold']))
        print(colored("| (___   /  \ | |    | |__| | | |    | |   ", "yellow",attrs=['bold']))
        print(colored(" \___ \ / /\ \| |    |  __  | | |    | |   ", "blue",attrs=['bold']))
        print(colored(" ____) / ____ \ |____| |  | |_| |_   | |   ", "magenta", attrs=['bold']))
        print(colored("|_____/_/    \_\_____|_|  |_|_____|  |_|          -Do good. Be Ethical.", "white", attrs=['bold']))
        print(colored("-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-\n", "cyan", attrs=['bold']))

    def logo4():
        
        print(colored("═════════════════════════════════════════════════════", "cyan", attrs=['bold']))
        print(colored("  _____         _____ _    _ _____ _______ ", "magenta" , attrs=['bold']))
        print(colored(" / ____|  /\   / ____| |  | |_   _|__   __|", "green", attrs=['bold']))
        print(colored("| (___   /  \ | |    | |__| | | |    | |   ", "cyan",attrs=['bold']))
        print(colored(" \___ \ / /\ \| |    |  __  | | |    | |   ", "yellow",attrs=['bold']))
        print(colored(" ____) / ____ \ |____| |  | |_| |_   | |   ", "blue", attrs=['bold']))
        print(colored("|_____/_/    \_\_____|_|  |_|_____|  |_|          -Do good. Be Ethical.", "red", attrs=['bold']))
        print(colored("═════════════════════════════════════════════════════\n", "cyan", attrs=['bold']))


    #animators
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
    print(colored("   ═════════════════════════════════════════════════════", "white", attrs=['bold']))
    print(colored("    ____        _____ _____  _____ _____", "magenta" , attrs=['bold']))
    print(colored("   |  _ \  _ __|  ___|_ _\ \/ /_ _|_   _|", "green", attrs=['bold']))
    print(colored("   | | | || '__| |_   | | \  / | |  | |  ", "cyan",attrs=['bold']))
    print(colored("   | |_| || |  |  _|  | | /  \ | |  | |  ", "yellow",attrs=['bold']))
    print(colored("   |____(_)_|  |_|   |___/_/\_\___| |_| ", "blue", attrs=['bold']))
    print(colored("   ═════════════════════════════════════════════════════\n", "white", attrs=['bold']))
                
                









#=========================================================================================================================================================

drprompt = "DRFIXIT ~|"
continuePrompt = "\nPress Any Key to continue "
ain = "Already Installed"



#classes

class snapp():
    def __init__(self):
        print("checking snapd is installed or not.")
        time.sleep(4)
        if not shutil.which('snap'):
            print("Not installed installing it...")
            self.install()
            print("Installed neccessary tool")
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    
    def install(self):
        os.system("sudo apt install snapd && sudo systemctl enable --now snapd apparmor")


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


class inssnap():
    def __init__(self):
        
        if not shutil.which('snap'):
            self.install() 
    def install(self):
        os.system("sudo apt install snap")





class drfix:
    def __init__(self):
        clearScr() #clear
        inssnap() #check if snap is installed
        logo()   #banner animation
        clearScr() #clear screen
        banr()   #drfixit banner
        print (color.GREEN + '''
  〘-------------≪⊶≼ Programmed By SACHIT ≽⊷≫-------------〙
    ''' + color.CYAN + '''
                      ______
                     |ERRORS|
               
       〘1〙═〢Errors while running apt update command
       〘2〙═〢Update/ full upgrade linux
       〘3〙═〢FIX no sound output
       〘4〙═〢Bluetooth not working/ can't turn on
            ══════════════════════════
            |sᴏғᴛᴡᴀʀᴇs/ᴀᴘᴘ sᴛᴏʀᴇ ғᴏʀ ʟɪɴᴜx|
            ══════════════════════════ 
            ════════════════════════════ 
           |ᴄᴀᴛᴀɢᴏʀɪᴇs ᴏғ sᴏᴛᴡᴀʀᴇs ᴛᴏ ɪɴsᴛᴀʟʟ|
            ════════════════════════════
            
       〘5〙═〢Multimedia
       〘6〙═〢Office
       〘7〙═〢Internet
       〘8〙═〢Developing/programming softwares
       〘9〙═〢Utility Softwares
       〘0〙═〢UPDATE SNAP
       〘00〙═〢CONTRIBUTORS
       〘99〙═〢EXIT\n
     ''')
        usrinput = input(drprompt)
        clearScr()
        if usrinput == "5":
            Multimedia()
        elif usrinput == "6":
            office()
        elif usrinput == "7":
            internet()
        elif usrinput == "8":
            dev()
        elif usrinput == "9":
            snapp()
        elif usrinput == "3":
            fixerr.nosound()
        elif usrinput == "4":
            fixerr.bt()    

        elif usrinput == "2":
            fixerr.update()    
        elif usrinput == "0":
            snapupdate()
        elif usrinput == "00":
            cont()
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
        input("Completed, press any key  to go back")
        self.__init__()    

#-----------------------



def cont():
    print(colored("Greet's to Manjaro_[Brahma]", "green", attrs=['bold']))



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
        print("  〘88〙═〢Back To Main Menu \n")
        usrinput2 = input(drprompt)
        clearScr()
        if usrinput2 == "1":
            vlc()
        elif usrinput2 == "2":
            spotify()
        elif usrinput2 == "3":
            Rythmbox()
        elif usrinput2 == "4":
            GIMP()
        elif usrinput2 == "5":
            adcity()
        
        elif usrinput2 == "88":
            drfix()
        else:
            self.__init__()
        self.completed()
    def completed(self):
        input(color.GREEN+"Completed, press anykey to go back")
        self.__init__()
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
#---------------
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
    / _ \|  ___|  ___|_ _/ ___| ____|
    | | | | |_  | |_   | | |   |  _|  
    | |_| |  _| |  _|  | | |___| |___ 
    \___/|_|   |_|   |___\____|_____ |

    '''

    def __init__(self):
        clearScr()
        print(color.GREEN+self.banner)

        print("  {1}--Libre office (alternative for MS office)")
    
        print("  {77}-Back To Main Menu \n")


        usrinput3= input(drprompt)
        clearScr()
        if usrinput3 == "1":
            libof()       
        elif usrinput3 == "77":
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





#=----------------------------------------------------------------------
class internet():
    banner = '''
     ___ _   _ _____ _____ ____  _   _ _____ _____
    |_S_| \ | |_ A _| _C__|  H \| \H| | __I_|_ T  _|
     | ||  \| | | | |  _| | |_) |  \| |  _|   | |
     | || |\  | | | | |___|  _ <| |\  | |___  | |  
    |___|_| \_| |_| |_____|_| \_\_| \_|_____| |_|  
    '''


    def __init__(self):
            clearScr()
            print(color.LYELLOW+self.banner)

            print("  {1}--Google Chrome")
            print("  {4}--Mozilla Firefox")
            print("  {3}--Chromium")
            print("  {4}--Thundermail mailer ")
            print("  {5}--Discord")
            print("  {6}--Brave Browser")
            print("  {7}--Opera browser")
            print("  {88}-Back To Main Menu \n")


            usrinput4 = input(drprompt)
            clearScr()
            if usrinput4 == "1":

                gchrome()
            elif usrinput4 == "4":

                mozilla()
            elif usrinput4 == "3":

                Chromium()
            elif usrinput4 == "4":

                thmailer()
            elif usrinput4 == "5":

                discord()
            elif usrinput4 == "6":
                bravebrowser()

            elif usrinput4 == "88":
                drfix()
            else:
                self.__init__()
            self.completed()

    def completed(self):
            input(color.LYELLOW+"Completed,press anykey to go back")
            self.__init__()    


#sub class for INTERNET

class gchrome():
    def __init__(self):
        print(color.GREEN+"Checking if google chrome is installed or not...")
        if not shutil.which('google-chrome'):
            self.install()
            
        else:
            print(ain)
    def install(self):
        print("downloading chrome...")
        os.system("curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o a.deb ")
        print("Downloaded ! installing it")
        os.system("sudo dpkg -i a.deb")
        os.system("sudo rm -rf a.deb")
        print("All done !!")


class mozilla():
    def __init__(self):
        print(color.GREEN+"Checking if firefox is installed or not...")
        if not shutil.which('firefox'):
            self.install()
            
        else:
            print(ain)
        
    def install(self):
        print("working on this...wait for update") 



class bravebrowser():
    print(color.GREEN+"Checking if Bravebrowser is installed or not...")
    def __init__(self):
        if not shutil.which('brave-browser'):
            self.install()
            
        else:
            print(ain)
 
    def install(self):
        print("brave is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install brave")
        print("Brave browser installed !")

class Chromium():
    def __init__(self):
        print(color.GREEN+"Checking if Chromium is installed or not...")
        if not shutil.which('chromium'):
            self.install()
            
        else:
            print(ain)
    def install(self):
        print("Chromium is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install chromium")
        print("Chromium browser installed !")



class thmailer():
    def __init__(self):
        print(color.GREEN+"Checking if thundebird mailer is installed or not...")
        if not shutil.which('thunderbird'):
            self.install()
            
        else:
            print(ain)
            
           
    def install(self):
        print(" is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install thunderbird ")
        print("Thunderbird mailer installed !")

class opera():
    def __init__(self):
        print(color.GREEN+"Checking if Opera is installed or not...")
        if not shutil.which(''):
            self.install()
            
        else:
            print(ain)
            
            

   


    def install(self):
        print("Opera is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install opera")
        print(" installed !")


#-------------------------------------------------------------------------------------------------------------


#class development and programming

class dev():
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
            print(color.LMAGENTA+self.banner)

            print("  〘1〙═〢 Pycharm CE")
            print("  〘2〙═〢 VS code")
            print("  〘3〙═〢 Sublime text")
            print("  〘4〙═〢 Beekeeper Studio ")
            print("  〘5〙═〢 Android Studio")
            print("  〘6〙═〢 Php Storm")
            print("  〘7〙═〢 Flutter")
            print("  〘8〙═〢 Atom")
            print("  {88}-Back To Main Menu \n")


            usrinput5 = input(drprompt)
            clearScr()
            if usrinput5 == "1":
                pycharm()

            elif usrinput5 == "4":
                vscode()

            elif usrinput5 == "3":
                sublimetext()

            elif usrinput5 == "4":
                bkstudio()

            elif usrinput5 == "5":
                andstudio()
                
            elif usrinput5 == "6":
                phpstorm()
            
            elif usrinput5 == "7":
                Flutter()

            elif usrinput5 == "8":
                atom()    



            elif usrinput5 == "88":
                drfix()


            else:
                self.__init__()
            self.completed()

    def completed(self):
            input(color.GREEN+"Completed,press anykey to go back")
            self.__init__()    



##sub classes for development and programming softwares

class pycharm():
    def __init__(self):
        print(color.GREEN+"Checking if Pycharm is installed or not...")
        if not shutil.which(''):
            self.install()
            
        else:
            print(color.GREEN+ain)
 
    def install(self):
        print(color.GREEN+"Pycharm CE is not installed !!")
        time.sleep(1.5)
        print(color.GREEN+"Installing...")
        os.system("sudo snap install pycharm-community --classic")
        print(color.GREEN+" Pycharm CE installed !")


class vscode():
    def __init__(self):
        print(color.GREEN+"Checking if visual studio code is installed or not...")
        if not shutil.which('code'):
            self.install()
        else:
            print(color.GREEN+ain)
            response = input(continuePrompt)
 
    def install(self):
        print(color.LYELLOW+"Vs code is not installed !!")
        time.sleep(1.5)
        print(color.LYELLOW+"Installing...")
        os.system("sudo snap refresh && sudo snap install code --classic")
        print(color.LYELLOW+"Visual studio code installed !!")    

        
                 
class sublimetext():
    def __init__(self):
        print(color.GREEN+"Checking if Sublime text is installed or not...")
        if not shutil.which(''):
            self.install()
        else:
            print(color.GREEN+ain)
            response = input(continuePrompt)
 
    def install(self):
        print(color.LYELLOW+"Sublime text is not installed !!")
        time.sleep(1.5)
        print(color.LYELLOW+"Installing...")
        os.system("sudo snap refresh && sudo snap install sublime-text --classic")
        print(color.LYELLOW+"Sublime text installed !!") 



class andstudio():
    def __init__(self):
        print(color.GREEN+"Checking if Android Studio is installed or not...")
        if not shutil.which('android-studio'):
            self.install()
        else:
            print(color.GREEN+ain)
 
    def install(self):
        print(color.LYELLOW+"Android Studio is not installed !!")
        time.sleep(1.5)
        print(color.LYELLOW+"Installing...")
        os.system("sudo snap refresh && sudo snap install android-studio --classic")
        
   
           








































































































if __name__ == "__main__":
    try:
        
        drfix()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.45)        
        
