import os
import sys
import platform
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


github_url = "https://github.com/Applehx7"


if __name__ == '__main__':
    print(bcolors.FAIL+"Please run ktool2.py, simply type python ktool2.py"+bcolors.ENDC)
    sys.exit()


def banner():
    print(bcolors.HEADER +
          """
             __    __   __                          __   ______  
            |  \  /  \ |  \                        |  \ /      \ 
            | $$ /  $$_| $$_     ______    ______  | $$|  $$$$$$\\
            | $$/  $$|   $$ \   /      \  /      \ | $$ \$$__| $$
            | $$  $$  \$$$$$$  |  $$$$$$\|  $$$$$$\| $$ /      $$
            | $$$$$\   | $$ __ | $$  | $$| $$  | $$| $$|  $$$$$$ 
            | $$ \$$\  | $$|  \| $$__/ $$| $$__/ $$| $$| $$_____ 
            | $$  \$$\  \$$  $$ \$$    $$ \$$    $$| $$| $$     \\
            \$$   \$$   \$$$$   \$$$$$$   \$$$$$$  \$$ \$$$$$$$$"""
          + bcolors.ENDC
          )
    print(bcolors.HEADER + "\n\t\t\t+[+[+[ Applehx07 Ducky ]+]+]+" + bcolors.ENDC)
    print(bcolors.HEADER + f"\t+[+[+[ GITHUB:{github_url} ]+]+]+" + bcolors.ENDC)
    print(bcolors.HEADER + f"\t\t\t  PRESS ctrl+c to Cancel" + bcolors.ENDC + "\n\n")


def tool_ins():
    os.system('clear')
    banner()
    print(
        bcolors.OKBLUE +
        """
    1/ Install Kali Linux Tools.
    2/ Install Kali Linux All Tools.
    3/ Install Kali Meta packages.
    4/ Add Kali/Blackarch Repository
    0/ EXIT...
        """ + bcolors.ENDC
    )
    user_inp = input(bcolors.OKCYAN + "\t--->> " + bcolors.ENDC)
    while int(user_inp) > 4 or int(user_inp) < 0:
        print(bcolors.FAIL + "\tINVALID INPUT! TRY AGAIN..." + bcolors.ENDC)
        user_inp = input(bcolors.OKCYAN + "\t--->> " + bcolors.ENDC)

    if int(user_inp) == 0:
        print(bcolors.WARNING + "\n\t EXITING.... ( ͡° ᴥ ͡°)" + bcolors.ENDC)
        sys.exit()
    else:
        return (user_inp)


def detect_os():
    oss = platform.system()
    if oss != 'Linux':
        print(bcolors.FAIL + "\tOperating SYSTEM NOT SUPPORTED!!" + bcolors.ENDC)
        sys.exit()
    file = open("/etc/os-release")
    file_content = file.read()
    file.close()
    dictionary = {}
    spl = file_content.split("\n")
    for i in range(len(spl)-1):
        tup = (tuple(spl[i].split('=')))
        dictionary[tup[0]] = tup[1]
    if dictionary['ID_LIKE'].strip() != 'arch' and dictionary['ID_LIKE'] != 'debian':
        print(bcolors.FAIL + "\tOperating SYSTEM NOT SUPPORTED!!" + bcolors.ENDC)
        sys.exit()
    else:
        return dictionary['ID_LIKE']


def add_repo(op_sys):
    os.system('clear')
    banner()
    if op_sys == 'arch':
        print(bcolors.OKBLUE + "\tAdding Blackarch repo...!" + bcolors.ENDC)
        os.system('curl -O https://blackarch.org/strap.sh')
        os.system('chmod +x strap.sh')
        os.system('./strap.sh')
        print(bcolors.OKBLUE + "\tUpdating System...!" + bcolors.ENDC)
        os.system('pacman -Syyu')
        print(bcolors.OKBLUE + "\tAdding Blackarch repo Completed...!" + bcolors.ENDC)
    elif op_sys == 'debian':
        print(bcolors.OKBLUE + "\tAdding Kali Linux repo..." + bcolors.ENDC)
        os.system("echo '# Kali linux repositories | Added by Ktool2' >> /etc/apt/sources.list")
        os.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
        os.system("apt update")
        print(bcolors.OKBLUE + "\tDONE...!" + bcolors.ENDC)
    else:
        sys.exit()


def root_detect():
    os.system('clear')
    banner()
    if os.getuid() != 0:
        print(bcolors.FAIL + "error: you cannot perform this operation unless you are root." + bcolors.ENDC)
        sys.exit()


def check_response(url):
    if requests.get(url).ok != True:
        print(f"Connection Problem... {url}")
        exit()
    else:
        print(bcolors.OKGREEN + "Website Response: OK" + bcolors.ENDC)
