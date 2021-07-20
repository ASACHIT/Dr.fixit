import os
import shutil
import time


class color:

    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[36m"
    WHITE = "\033[97m"
    LYELLOW = "\033[93m"
    XYZ = "\033[96m"
    LMAGENTA = "\033[95m"


def clr():
    os.system("clear")


class nosound:
    def __init__(self):
        print(color.GREEN + "Checking distro...")
        if not shutil.which("apt"):
            print(
                "this section is only made for distro based on apt package manager :(."
            )

        else:
            self.fixsound()

    def fixsound():

        time.sleep(2)
        print(color.GREEN + "Installing pulse audio_audio manager")
        time.sleep(2)
        os.system("sudo apt install pulseaudio")
        print(color.CYAN + "Turning on pulse audio and its services")
        time.sleep(2)
        os.system(
            "sudo systemctl --user enable pulseaudio && systemctl --user start pulseaudio"
        )
        time.sleep(2)
        clr()
        time.sleep(1)
        print(color.GREEN + "Check if sound is available in output !!")
        time.sleep(4.5)
        print(color.GREEN + "that was at least i could do :)")
        time.sleep(4)
        print(color.GREEN + "IF, it wasn't fix, try rebooting your system..")
        time.sleep(4)


def bt():
    clr()
    time.sleep(2)
    print(color.GREEN + "searching For issue in Bluetooth")
    time.sleep(2)
    print(color.GREEN + "Restarting Bluetooth manager services")
    time.sleep(3)
    try:
        os.system("sudo service bluetooth restart ")
    except os.error:
        print("sorry, this section was only for distro based on apt package manager")
        time.sleep(2)
        print(
            "\nplease submitt issue in this link- https://github.com/SACHIT69/Dr.fixit/issues ||Any feedback would be greatly appreciated. Thank you"
        )
        time.sleep(5)

    time.sleep(3)
    print(color.GREEN + "Check if bluetooth is enabled or not..")
    time.sleep(3)


def uperror():
    clr()
    print(color.CYAN + "error while updating packages?,and while installing packages?")
    time.sleep(2)
    print(color.GREEN + "wait, i will fix this..")
    print(color.GREEN + "working on issue...")
    time.sleep(3)
    print(color.GREEN + "wait a while, this may take more time !")
    time.sleep(1.5)
    try:
        os.system("sudo apt update --fix-missing && sudo apt --fix-broken install")
    except os.error:
        print(
            "i'm sorry, this section was only for distro based on apt package manager :( "
        )
        time.sleep(2)
        print(
            "\nplease submitt issue in this link- https://github.com/SACHIT69/Dr.fixit/issues ||Any feedback would be greatly appreciated. Thank you"
        )
        time.sleep(3)

    time.sleep(2)
    print(color.CYAN + "Everything done.. !!")


def update():
    clr()
    print(color.GREEN + "updating...")
    time.sleep(3)
    print(color.GREEN + "This may take more time, wait..")
    time.sleep(1.5)
    try:
        os.system(
            "sudo apt update -y && sudo apt full-upgrade -y && sudo apt dist-upgrade -y"
        )
    except os.error:
        print(
            "sorry :(. this command only runs in distor based in apt package manager")
        time.sleep(2.5)

    print(color.GREEN + "DONE !!")
    time.sleep(2.5)
