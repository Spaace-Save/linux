from typing import Tuple
import json
from getpass import getpass


def user_input() -> Tuple[str, str, str, str, bool, str, str, str, bool, bool]:
    print("\033[95m" + "Welcome to Eupnea" + "\033[0m")
    print("\033[95m" + "This script will help you create a bootable USB Stick/SD card for Eupnea" + "\033[0m")
    print("\033[95m" + "Please answer the following questions." "\033[0m")
    print("(If you dont know what to answer, just press enter and the recommended answer will be used)")
    print("\033[92m" + "Which Linux distro(flavor) would you like to use?" + "\033[0m")
    # setting optional vars to 0
    distro_version = 0
    use_openbox = False
    rebind_search = False
    create_iso = True
    distro_link = ""
    username = ""
    password = ""
    while True:
        distro_name = input(
            "\033[94m" + "Available options: Ubuntu(default, recommended), Debian, Arch, Fedora(cli only)\n" +
            "\033[0m")
        match distro_name:
            case "Ubuntu" | "ubuntu" | "":
                print("Ubuntu selected")
                distro_name = "ubuntu"
                print("\033[92mUse latest version?\033[0m")
                temp_input = input("\033[94mPress enter for yes, or type in the version number(for example: '21.10'):\n"
                                   + "\033[0m")
                if temp_input == "":
                    distro_version = "22.04"
                    distro_link = "jammy"
                    print("Using latest version: " + distro_version)
                    break
                else:
                    with open("distros.json", "r") as file:
                        distros = json.load(file)
                    if temp_input in distros["ubuntu"]:
                        distro_version = temp_input
                        distro_link = distros["ubuntu"][distro_version]
                        print("Using version: " + distro_version + " codename: " + distros["ubuntu"][temp_input])
                        break
                    else:
                        print("\033[93m" + "Version not available, please choose another" + "\033[0m")
                        continue
            case "Debian" | "debian":
                print("Debian selected")
                break
            case "Arch" | "arch" | "arch btw":
                print("Arch selected")
                break
            case "Fedora" | "fedora":
                print("Fedora selected")
                if input("\033[93mWarning: No desktop environment available for Fedora" + "\033[94m" +
                         "\nType 'yes' to continue or Press Enter to choose another distro(" + "\033[0m\n") == "yes":
                    print("Fedora confirmed")
                    temp_input = input("\033[92mUse latest version?" + "\033[94m" + "\nPress enter for yes, " +
                                       "or type in the version number(for example: '35'). " +
                                       "Versions 32 and 33 are not available:\n" + "\033[0m")
                    if temp_input == "":
                        distro_version = "36"
                        print("Using version: " + distro_version)
                        break
                    else:
                        with open("distros.json", "r") as file:
                            distros = json.load(file)
                        if temp_input in distros["fedora"]:
                            distro_version = temp_input
                            print("Using version: " + distro_version)
                            break
                        else:
                            print("\033[93m" + "Version not available, please choose another" + "\033[0m")
                            continue
                else:
                    print("\033[93mFedora not confirmed, please select another distro" + "\033[0m")
                    continue
            case _:
                print("\033[93mCheck your spelling and try again" + "\033[0m")
                continue
    # TODO: add per distro selections
    print("\033[92m" + "Which desktop environment would you like to use?" + "\033[0m")
    while True:
        de_name = input("\033[94mAvailable options: Gnome(default, recommended), KDE(recommended), MATE," +
                        " Xfce(recommended for weak devices), LXQt(recommended for weak devices), deepin, budgie, " +
                        "minimal, cli" + "\033[0m" + "\n")
        match de_name:
            case "Gnome" | "gnome" | "":
                print("Gnome selected")
                de_name = "gnome"
                # if input("\033[92m" + "Replace default window manager with OpenBox?(NOT RECOMMENDED)" + "\033[94m"
                #          + "\nType 'yes'. Press enter to use the default window manager instead.\033[0m\n") == "yes":
                #     print("Openbox + Gnome selected")
                #     use_openbox = True
                # else:
                #     print("Using the default window manager")
                #     use_openbox = False
                break
            case "KDE" | "kde":
                print("KDE selected")
                de_name = "kde"
                # if input("\033[92m" + "Replace default window manager with OpenBox?(NOT RECOMMENDED)" + "\033[94m"
                #          + "\nType 'yes'. Press enter to use the default window manager instead.\033[0m\n") == "yes":
                #     print("Openbox + KDE selected")
                #     use_openbox = True
                # else:
                #     print("Using the default window manager")
                #     use_openbox = False
                break
            case "MATE" | "mate":
                print("MATE selected")
                de_name = "mate"
                break
            case "xfce" | "Xfce":
                print("Xfce selected")
                de_name = "xfce"
                break
            case "lxqt" | "Lxqt":
                print("Lxqt selected")
                de_name = "lxqt"
                break
            case "deepin":
                print("Deepin selected")
                de_name = "deepin"
                break
            case "budgie":
                print("Budgie selected")
                de_name = "budgie"
                break
            case "minimal":
                print("Minimal selected")
                de_name = "minimal"
                break
            case "cli" | "none":
                print("CLI selected")
                if input("\033[93mWarning: No desktop environment will be installed" + "\033[94m\nType 'yes' to " +
                         "continue or Press Enter to choose a desktop environment" + "\033[0m\n") == "yes":
                    print("No desktop will be installed")
                    de_name = "cli"
                    break
            case _:
                print("\033[93m" + "Check your spelling and try again" + "\033[0m")
    # Ubuntu + gnome now has a first time setup, so skip this part for ubuntu with gnome
    if not distro_name == "ubuntu" and not de_name == "gnome":
        print("\033[92m" + "Enter username to be used in Eupnea" + "\033[0m")
        while True:
            username = input("\033[94m" + "Username(default: 'localuser'): " + "\033[0m")
            for char in username:
                if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-":
                    print("\033[93m" + "Username contains invalid character: " + char + "\033[0m")
                    break
            if username == "":
                print("Using localuser as username")
                username = "localuser"
                break
            else:
                break

        print("\033[92m" + "Please set a secure password" + "\033[0m")
        while True:
            passwd_temp = getpass("\033[94m" + "Password: " + "\033[0m")
            if passwd_temp == "":
                print("\033[93m" + "Password cannot be empty" + "\033[0m")
                continue
            else:
                passwd_temp_2 = getpass("\033[94m" + "Repeat password: " + "\033[0m")
                if passwd_temp == passwd_temp_2:
                    password = passwd_temp
                    print("Password set")
                    break
                else:
                    print("\033[93m" + "Passwords do not match, try again" + "\033[0m")
                    continue

    print("\033[92m" + "Enter hostname for the chromebook.(Hostname is something like a device name)" + "\033[0m")
    while True:
        hostname = input("\033[94m" + "Hostname(default: 'eupnea-chromebook'): " + "\033[0m")
        if hostname == "":
            print("Using eupnea-chromebook as hostname")
            hostname = "eupnea-chromebook"
            break
        if hostname[0] == "-":
            print("\033[93m" + "Hostname cannot start with a '-'" + "\033[0m")
            continue
        for char in hostname:
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-":
                print("\033[93m" + "Hostname contains invalid character: " + char + "\033[0m")
                break
        else:
            break

    print(
        "\033[92m" + "Would you like to rebind the Search/Super(Win key) key to Caps Lock?(NOT RECOMMENDED)" + "\033[0m")
    while True:
        if input("\033[94m" + "Type yes to rebind. Press enter to keep old binding" "\033[0m" + "\n") == "yes":
            print("Search key will be a CAPS LOCK key")
            rebind_search = True
        else:
            print("Search key will be Super/Win key")
            rebind_search = False
        break

    print("\033[92m" + "Create image or write to the SD-card/USB-stick directly? (direct write is not yet supported)"
          + "\033[0m")
    while True:
        if input("\033[94m" + "Type 'direct' to use write directly. " +
                 "Press Enter to create an img file" "\033[0m" + "\n") == "direct":
            print("USB selected")
            create_iso = False
        else:
            print("Image selected")
        break
    print("User input complete")
    return distro_name, distro_version, distro_link, de_name, use_openbox, username, password, hostname, \
           rebind_search, create_iso


if __name__ == "__main__":
    print("\033[91m" + "Do not run this file. Run build.py" + "\033[0m")