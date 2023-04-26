import os
import defs
import scrap

#Check If user is root or not
defs.root_detect()

tools = scrap.tools_name()
op_s = defs.detect_os()

if tools[1] == 1 or tools[1] == 2:
    os.system('clear')
    defs.banner()
    print(defs.bcolors.OKGREEN + "\tInstalling Kali Linux tools..." + defs.bcolors.ENDC)
    for i in tools[0]:
        print(defs.bcolors.WARNING + f"\tInstalling {i}..." + defs.bcolors.ENDC)
        os.system(f"apt install {i}" if op_s == 'debian' else f"pacman -S {i}")
    print(defs.bcolors.WARNING + f"\tInstalled {i}..." + defs.bcolors.ENDC)


