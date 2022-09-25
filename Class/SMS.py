import requests
import os
from bs4 import BeautifulSoup
from time import sleep

YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'


class CLEAR():

    def clear():
        if os.name == 'posix':
            os.system('clear')
            # else screen will be cleared for windows
        else:
            os.system('cls')

    def countdown_M(t):
        print("\n ")
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{YELLOW}[TIMER] {WHITE}This process will take {RED}[ {WHITE}{mins} Min {secs}s{RED} ]{WHITE} to make sure the code will arrived =){WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            t -= 1

    def countdown_S(t):
        print("\n ")
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{BOLD}{YELLOW}[TIMER] {WHITE} Please wait For {RED}[ {WHITE}{secs}s{RED} ] {WHITE}to get the result{WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            t -= 1


class SMS():

    def main(self, id):
        url = f"https://www.receivesms.co/us-phone-number/{id}/"
        body = requests.get(url).text
        soup = BeautifulSoup(body, 'html.parser')

        CLEAR.clear()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"{GREEN}[INFO] {WHITE}Your number is {self}\n")

        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            CLEAR.countdown_S(3)
            time = soup.find_all('div', class_="col-xs-0 col-md-2 mobile_hide")
            message = soup.find_all('div', class_="col-xs-12 col-md-8")
            print("\n"+"="*60)
            for n in range(0, 10):
                v1 = f"{time[n].get_text()}"
                arrived = v1.splitlines()[0]
                v2 = f"{message[n].get_text()}"
                Content = v2.splitlines()[0]
                print("\n"+"-"*20)
                print(f"\n{GREEN}[+] {WHITE}Message : {Content}{YELLOW}")
                print(f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")
            print("\n"+"="*60)
       
            check = str(input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
            if check == "n":
                CLEAR.clear()
                CLEAR.countdown_M(3)
                print("\n\n"+"="*60)
                print(f"\n{YELLOW}{BOLD}[RESULT] {WHITE}Code Result: \n")
                for n in range(0, 10):
                    v1 = f"{message[n].get_text()}"
                    arrived = v1.splitlines()[0]
                    v2 = f"{time[n].get_text()}"
                    Content = v2.splitlines()[0]
                    print("\n"+f"{YELLOW}-{WHITE}"*20)
                    print(f"\n{GREEN}[+] {WHITE}Message : {Content}{YELLOW}")
                    print(
                        f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")

                print("\n"+"="*60)
                print(
                    f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                print(
                    f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")

            if check == "y":
                print(f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")

        else:
            print(f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")