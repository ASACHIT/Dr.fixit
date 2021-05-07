from termcolor import colored #module for colored text
import os 
import time
import subprocess
import getpass
from sys import argv
#banner animation

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

    def logo2():
        
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
    logo2()
    time.sleep(1)
    subprocess.run(["clear"])
    logo1()
    time.sleep(1)
    subprocess.run(["clear"])
    logo2()


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
        time.sleep(2)
        if not self.installed():
            print("Not installed installing it...")
            self.install()
            print("Installed neccessary tool")
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/"))

    def install(self):
        os.system("sudo apt install snapd && sudo systemctl enable --now snapd apparmor")


class color:
    
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[36m'


def clearScr():
    os.system('clear')







class drfix:
    def __init__(self):
        clearScr()
        logo()
        snapp()
        clearScr()
        time.sleep(1)
        banr()
        
        print (color.GREEN + '''
  〘-------------≪⊶≼ Programmed By SACHIT ≽⊷≫-------------〙
    ''' + color.CYAN + '''
                      ______
                     |ERRORS|
               
       〘1〙═〢Errors while running apt update command
       〘2〙═〢Update/ full upgrade linux
       〘3〙═〢FIX no sound output
       〘4〙═〢Bluetooth not working/ can't turn on
            ═════════════════════════
            |sᴏғᴛᴡᴀʀᴇs/ᴀᴘᴘ sᴛᴏʀᴇ ғᴏʀ ʟɪɴᴜx|
            ═════════════════════════ 
            ═══════════════════════════ 
           |ᴄᴀᴛᴀɢᴏʀɪᴇs ᴏғ sᴏᴛᴡᴀʀᴇs ᴛᴏ ɪɴsᴛᴀʟʟ|
            ═══════════════════════════
            
       〘5〙═〢Multimedia
       〘6〙═〢Office
       〘7〙═〢Internet
       〘8〙═〢Developing/programming softwares
       〘9〙═〢Utility Softwares
       〘0〙═〢INSTALL & UPDATE
       〘〙═〢CONTRIBUTORS
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
            webdv()
        elif usrinput == "5":
            utility()
        elif usrinput == "6":
            webHackingMenu()
        elif usrinput == "7":
            a()
        elif usrinput == "8":
            b()
        elif usrinput == "0":
            c()
        
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
        input("Completed, click return to go back")
        self.__init__()    



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
        print(self.banner)

        print("  {1}--VLC media player")
        print("  {2}--spotify")
        print("  {3}--Rythmbox (music player)")
        print("  {4}--GIMP- GNU image Manipulation program(photoshop alternative) ")
        print("  {5}--Audacity (Audio software for multi-track recording and editing)")
        print("  {88}-Back To Main Menu \n")


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
            Audacity()
        
        elif usrinput2 == "88":
            drfix()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        input("Completed, click return to go back")
        self.__init__()

class vlc:
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/vlc"))

    def install(self):
        os.system("sudo snap install vlc")

class spotify:
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/spotify"))  

    def install(self):
        os.system("sudo snap install spotify")    




class Rythmbox:
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/.local/share/rhythmbox/"))

    def install(self):
        os.system("sudo apt install rhythmbox")                       


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
        print(self.banner)

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
        input("Completed, click return to go back")
        self.__init__()

class libof():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/libreoffice"))

    def install(self):
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
            print(self.banner)

            print("  {1}--Google Chrome")
            print("  {2}--Mozilla Firefox")
            print("  {3}--Chromium")
            print("  {4}--Thundermail mailer ")
            print("  {5}--Discord")
            print("  {6}--Brave Browser")
            print("  {7}--Opera browser")
            print("  {88}-Back To Main Menu \n")


            usrinput2 = input(drprompt)
            clearScr()
            if usrinput2 == "1":

                gchrome()
            elif usrinput2 == "2":

                mozilla()
            elif usrinput2 == "3":

                Chromium()
            elif usrinput2 == "4":

                thmailer()
            elif usrinput2 == "5":

                discord()
            elif usrinput2 == "6":
                bravebrowser()

            elif usrinput2 == "88":
                drfix()
            else:
                self.__init__()
            self.completed()

    def completed(self):
            input("Completed, click return to go back")
            self.__init__()    


#sub class for INTERNET

class gchrome():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir("/etc/opt/chrome/"))

    def install(self):
        print("download chrome...")
        os.system("curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o a.deb ")
        print("Downloaded ! installing it")
        os.system("sudo dpkg -i a.deb")
        os.system("sudo rm -rf a.deb")
        print("All done !!")


class mozilla():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir("/usr/share/mozilla/"))

    def install(self):
        print("working on this...wait for update") 



class bravebrowser():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/brave"))

    def install(self):
        print("brave is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install brave")
        print("Brave browser installed !")






class Chromium():
    def __init__(self):
        if not self.installed() or self.installed2():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):                #to check in snap
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/chromium"))

    def installed2(self):             # to check if installed from other source
        return(os.path.isdir("/usr/share/chromium"))    

    def install(self):
        print("Chromium is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install chromium")
        print("Chromium browser installed !")



class thmailer():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):                #to check in snap
        usr = getpass.getuser()
        return (os.path.isdir(f""))

    

    def install(self):
        print(" is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install thunderbird ")
        print("Thunderbird mailer installed !")

class opera():
    def __init__(self):
        if not self.installed():
            self.install()
            
        else:
            print(ain)
            
            response = input(continuePrompt)

    def installed(self):                #to check in snap
        usr = getpass.getuser()
        return (os.path.isdir(f"/home/{usr}/snap/opera"))



    def install(self):
        print(" is not installed !!")
        time.sleep(1.5)
        print("Installing...")
        os.system("sudo snap install opera")
        print(" installed !")











































































































if __name__ == "__main__":
    try:
        
        drfix()
    except KeyboardInterrupt:
        print(" Finishing up...\n")
        time.sleep(0.25)        
        
