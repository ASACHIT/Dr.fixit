import os
import shutil
import time
import scripts.functions as er
import distro

from scripts import multimedia as mm

ain = "Already Installed"


class geany:
    def __init__(self):
        print(mm.color.GREEN + "Checking if geany is installed or not...")
        if not shutil.which("geany"):
            self.install()

        else:
            print(ain)

    def install(self):
        print("checking distro...")
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == "kali" or "ubuntu" or "debian":
            os.system("sudo apt install geany")

        elif dist == "arch" or "manjaro":
            os.system("sudo pacman -S geany")

        elif dist == "fedora":
            os.system("sudo snap install geany-gtk --edge")

        else:
            try:
                os.system("sudo snap install geany-gtk --edge")
            except OSError:
                er.issue("geany")
                exit()


class stacer:
    def __init__(self):
        print(mm.color.GREEN + "checking Stacer in system...")
        if not shutil.which("stacer"):
            self.install()

        else:
            print(ain)

    def install(self):
        print("checking distro...")
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == "kali":
            os.system("sudo apt install stacer")

        elif dist == "arch" or "manjaro":
            os.system("pacman -s stacer")

        elif dist == "fedora":
            os.system("yum install stacer")
        elif dist == "gentoo":
            os.system("emerge -av stacer")
        else:
            try:
                os.system("sudo apt install stacer")
            except:
                try:
                    os.system("sudo pacman -S Stacer")
                except:
                    er.issue("Stacer")
                    time.sleep(3)
                    print(
                        "you can install manually from here.. link- https://github.com/oguzhaninan/Stacer/releases")
                    time.sleep(3)
                    exit()


class obs:
    def __init__(self):
        print(mm.color.GREEN + "checking OBS in system...")
        if not shutil.which("obs-studio"):
            self.install()
        else:
            print(ain)

    def install(self):
        print("checking distro...")
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == "kali" or "ubuntu" or "mint" or "parrot":
            os.system("sudo snap install obs-studio")

        elif dist == "arch":
            os.system("sudo pacman -S obs-studio")

        elif dist == "fedora":
            os.system(
                " sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
            )
            os.system(
                "sudo dnf install obs-studio &&  sudo dnf install xorg-x11-drv-nvidia-cuda &&  sudo dnf install xorg-x11-drv-nvidia-340xx-cuda"
            )

        elif dist == "manjaro":
            os.system("sudo pacman -S obs-studio")

        else:
            try:
                os.system("sudo snap install obs-studio")
            except OSError:
                er.issue("OBS-studio")
                time.sleep(3)
                print(
                    "you can install manually from here.. link- https://obsproject.com/wiki/install-instructions#linux "
                )
                time.sleep(3)
                exit()


class msteam:
    def __init__(self):
        print(mm.color.GREEN + "checking teams in system...")
        if not shutil.which("teams"):
            self.install()

        else:
            print(ain)

    def install(self):
        print("checking distro...")
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == "kali" or "ubuntu" or "mint" or "parrot":
            os.system("sudo snap install teams")

        elif dist == "arch":
            os.system("sudo snap install teams")

        elif dist == "fedora":
            os.system("sudo snap install teams")

        elif dist == "manjaro":
            os.system("sudo snap install teams")

        else:
            try:
                os.system("sudo snap install teams")
            except OSError:
                er.issue("MS TEAM")
                time.sleep(3)
                print(
                    "you can install manually from here.. link- https://www.microsoft.com/en-ww/microsoft-teams/download-app "
                )
                time.sleep(3)
                exit()


class ksnip:
    def __init__(self):
        print(mm.color.GREEN + "checking ksnip in system...")
        if not shutil.which("ksnip"):
            self.install()

        else:
            print(ain)

    def install(self):
        print("checking distro...")
        dist = distro.linux_distribution(full_distribution_name=False)[0]

        if dist == "kali" or "ubuntu" or "mint" or "parrot":
            os.system("sudo snap install ksnip")

        elif dist == "arch":
            os.system("sudo snap install ksnip")

        elif dist == "fedora":
            os.system("sudo snap install ksnip")

        elif dist == "manjaro":
            os.system("sudo snap install ksnip")

        else:
            try:
                os.system("sudo snap install ksnip")
            except OSError:
                er.issue("Ksnip")
                time.sleep(3)
                exit()


class qbit:
    def __init__(self):
        print(mm.color.GREEN + "Checking Qbittorrent in your system...")
        if not shutil.which("qbittorrent"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("snap install qbittorrent-arnatious")
        except os.error:
            er.issue("qbittorrents")


class uget:
    def __init__(self):
        print(mm.color.GREEN + "Checking Uget in your system...")
        if not shutil.which("uget"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("snap install uget --edge")

        except os.error:
            er.issue("Uget")


class Gforce:
    def __init__(self):
        print(mm.color.GREEN + "checking Geforce in your system...")
        if not shutil.which("gforcenow"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            os.system("snap install geforcenow")

        except os.error:
            er.issue("Geforce now")


class handbrake:
    def __init__(self):
        print(mm.color.LYELLOW + "checking handbrake in your system...")
        if not shutil.which("handbrake"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            print(mm.color.LYELLOW + "Installing Handbrake in your system")
            os.system("snap install handbrake-jz")

        except os.error:
            er.issue("Handbrake")


class kedenlive:
    def __init__(self):
        print(mm.color.LYELLOW + "checking Kdenlive in your system...")
        if not shutil.which("kdenlive"):
            self.install()
        else:
            print(ain)

    def install(self):
        try:
            print(mm.color.LYELLOW + "Installing Handbrake in your system")
            os.system("snap install kdenlive")

        except os.error:
            er.issue("Kdenlive")
