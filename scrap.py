import os
import sys
import requests
from bs4 import BeautifulSoup
import defs

if __name__ == '__main__':
    print(defs.bcolors.FAIL+"Please run ktool2.py, simply type python ktool2.py"+defs.bcolors.ENDC)
    sys.exit()

def tools_name():
    user_inp = int(defs.tool_ins())


    if user_inp == 1:
        kali_url = 'https://www.kali.org/tools/'
        os.system('clear')
        defs.banner()
    elif user_inp == 2:
        kali_url = 'https://www.kali.org/tools/all-tools/'
        os.system('clear')
        defs.banner()
    elif user_inp == 3:
        #meta PACKAGES
        os.system("clear")
        defs.banner()
        import meta
        sys.exit()
    elif user_inp == 4:
        os.system('clear')
        defs.banner()
        defs.add_repo(defs.detect_os())
        sys.exit()
    elif user_inp == 0:
        print(defs.bcolors.OKCYAN + "Exiting..." + defs.bcolors.ENDC)
        sys.exit()
    else:
        print(defs.bcolors.FAIL+"An Error occured"+defs.bcolors.ENDC)
        sys.exit()

    kali_response = requests.get(kali_url)

    defs.check_response(kali_url)


    all_content = kali_response.content
    content = BeautifulSoup(all_content, 'html.parser')


    #Get All Tools DIV in an array
    all_tools_div = content.find_all('div', class_="card")

    tools_name = set()

    for i in all_tools_div:
        pkg = (i.find('a').find(string=True, recursive=False)).strip()
        tools_name.add(pkg)

    return tools_name, user_inp