import sys
import requests
import defs
import os
from bs4 import BeautifulSoup

if __name__ == '__main__':
    print(defs.bcolors.FAIL+"Please run ktool2.py, simply type python ktool2.py"+defs.bcolors.ENDC)
    sys.exit()

os.system('clear')
defs.banner()

if defs.detect_os() != 'debian':
    print(defs.bcolors.FAIL+"You Need to use a debian based distro to Insttall kali meta packages! Exiting..."+defs.bcolors.ENDC)
    sys.exit()

kali_url = 'https://www.kali.org/docs/general-use/metapackages/'
defs.check_response(kali_url)
kali_response = requests.get(kali_url)
allcon = kali_response.content
content = BeautifulSoup(allcon, 'html.parser')
li = (content.find('div', id='content').find_all('li'))
meta_pack_name = []
for i in li:
    meta_pack_name.append(i.code.text)

for i in range(len(meta_pack_name)):
    print(defs.bcolors.OKCYAN+f"{i+1}. {meta_pack_name[i]}")
print(defs.bcolors.OKCYAN+f"41. All")

install_pack_num = input(defs.bcolors.OKCYAN+"-->>"+defs.bcolors.ENDC)

if int(install_pack_num) != 41:
    print(defs.bcolors.WARNING+f"Installing {meta_pack_name[int(install_pack_num)-1]}"+defs.bcolors.ENDC)
    os.system(f"sudo apt install {meta_pack_name[int(install_pack_num)-1]}")
elif int(install_pack_num) == 41:
    print(defs.bcolors.WARNING + f"Installing All Packages" + defs.bcolors.ENDC)
    for i in meta_pack_name:
        print(defs.bcolors.WARNING + f"Installing {i}" + defs.bcolors.ENDC)
        os.system(f"sudo apt install {i}")
