import os
from os import system as bash
import subprocess as sp


def config(de_name: str, distro_version: str) -> None:
    print("\033[96m" + "Configuring Ubuntu" + "\033[0m")
    print("Installing packages")
    chroot("apt update -y")
    chroot("apt install -y network-manager tasksel software-properties-common sudo firmware-linux-free cloud-utils" +
           "firmware-linux-nonfree firmware-iwlwifi iw curl wget git")
    print("Reinstalling dbus")
    # TODO: Find out why reinstalling dbus is necessary
    chroot("apt reinstall -y dbus")
    print("Add non free repo")
    chroot("apt-add-repository non-free")
    chroot("apt update -y")
    # de install fails without updating apt
    print("\033[96m" + "Downloading and installing de, might take a while" + "\033[0m")
    match de_name:
        case "gnome":
            print("Installing gnome")
            # TODO: Maybe convert this to apt
            chroot("tasksel install desktop gnome-desktop")
        case "kde":
            print("Installing kde")
            chroot("apt install -y task-kde-desktop")
        case "mate":
            print("Installing mate")
            chroot("apt install -y mate-desktop-environment")
        case "xfce":
            print("Installing xfce")
            chroot("apt install -y task-xfce-desktop")
        case "lxqt":
            print("Installing lxqt")
            chroot("apt install -y task-lxqt-desktop")
        case "deepin":
            print("\033[91m" + "Deepin is not available for Debian" + "\033[91m")
            exit(1)
        case "budgie":
            print("Installing budgie")
            chroot("apt install budgie-desktop budgie-indicator-applet")
            # chroot("dpkg-reconfigure lightdm")
        case "minimal":
            print("Installing minimal")
            chroot("apt install -y xfce4 xfce4-terminal --no-install-recommends")
        case "cli":
            print("Installing nothing")
        case _:
            print("\033[91m" + "Invalid desktop environment!!! Remove all files and retry." + "\033[0m")
            exit(1)
    # Ignore libfprint-2-2 fprintd libpam-fprintd errors
    if not de_name == "cli":
        print("Setting system to boot to gui")
        chroot("systemctl set-default graphical.target")
    # GDM3 auto installs gnome-minimal. Gotta remove it if user didnt choose gnome
    if not de_name == "gnome":
        print("Fixing gdm3")
        try:
            os.remove("/mnt/eupnea/usr/share/xsessions/ubuntu.desktop")
        except FileNotFoundError:
            pass
        chroot("apt remove -y gnome-shell")
        chroot("apt autoremove -y")
    # TODO: Figure out why removing needrestart is necessary
    chroot("apt remove -y needrestart")
    print("Fixing securetty if needed")
    # "2>/dev/null" is for hiding error message, as not to scare the user
    bash("cp /mnt/eupnea/usr/share/doc/util-linux/examples/securetty /mnt/eupnea/etc/securetty 2>/dev/null")


def chroot(command: str) -> str:
    return sp.run(f'chroot /mnt/eupnea /bin/sh -c "{command}"', shell=True, capture_output=True).stdout.decode(
        "utf-8").strip()


if __name__ == "__main__":
    print("Do not run this file. Use build.py")
